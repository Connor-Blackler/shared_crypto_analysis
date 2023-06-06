from datetime import datetime
import numpy as np
from crypto_requests.request import get_historical_klines
from .indicator_options import OptionsRollingRisk


def _stat_calc(src, lookback):
    daily_return = src / src.shift(1) - 1
    daily_return.iloc[0] = 0  # first day of data, avoid NaN

    returns_array = []
    negative_returns_array = []
    positive_returns_array = []

    for i in range(len(daily_return) - 1, len(daily_return) - lookback - 2, -1):
        returns_array.append(daily_return[i])
        if daily_return[i] <= 0.0:
            negative_returns_array.append(daily_return[i])
        else:
            positive_returns_array.append(daily_return[i])

    # STAT CALCULATIONS
    standard_deviation = np.std(returns_array)
    negative_returns_standard_deviation = np.std(negative_returns_array)
    mean = np.mean(returns_array)
    sharpe = round(mean / standard_deviation * np.sqrt(lookback), 2)
    sortino = round(
        mean / negative_returns_standard_deviation * np.sqrt(lookback), 2)
    positive_area = sum(positive_returns_array)
    negative_area = sum(negative_returns_array) * (-1)
    omega = round(positive_area / negative_area, 2)

    return [sharpe, sortino, omega]


def get_inicator_rolling_risk(assets: list[str], options: OptionsRollingRisk = OptionsRollingRisk(),
                              quote_name: str = "USDT", start_date: str = "2021-06-01",
                              end_date: str = datetime.today().strftime('%Y-%m-%d'), interval: str = "1d"):

    output = []

    for asset in assets:
        data = get_historical_klines(asset,
                                     quote_name,
                                     start_date,
                                     end_date,
                                     interval)

        src = (data['High'] + data['Low'] + data['Close']) / 3

        results = _stat_calc(src, options.lookback)
        result_d = {
            "asset": asset,
            "sharp": results[0],
            "sortino": results[1],
            "omega": results[2]
        }

        output.append(result_d)

    return output
