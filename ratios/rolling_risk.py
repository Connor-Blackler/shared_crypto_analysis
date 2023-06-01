import numpy as np
from .binance_api import download_data


def stat_calc(src, lookback):
    daily_return = src / src.shift(1) - 1
    daily_return.iloc[0] = 0  # first day of data, avoid NaN

    returns_array = []
    negative_returns_array = []
    positive_returns_array = []

    for i in range(len(returns_array) - 1, len(returns_array) - lookback - 2, -1):
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


asset_name = 'BTC'
base_asset_name = 'USDT'
start_date = '2021-06-01'
end_date = '2023-06-02'
interval = '1d'

data = download_data(asset_name, base_asset_name,
                     start_date, end_date, interval)

src = (data['High'] + data['Low'] + data['Close']) / 3
# src = data['Close']

lookback = 30

results = stat_calc(src, lookback)
print("sharp: ", results[0], "\n",
      "sortino: ", results[1], "\n",
      "omega: ", results[2], "\n")
