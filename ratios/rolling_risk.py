import numpy as np
import pandas as pd
from .binance_api import download_data

desired_assets = ["BTC",
                  "ETH",
                  "BNB",
                  "XRP",
                  "ADA",
                  "DOGE",
                  "SOL",
                  "MATIC",
                  "LTC",
                  "TRX",
                  "DOT",
                  "SHIB",
                  "AVAX",
                  "LINK",
                  "ATOM",
                  "UNI",
                  "XMR",
                  "XLM",
                  "BCH",
                  "ICP",
                  "LDO",
                  "FIL",
                  "APT",
                  "HBAR",
                  "NEAR",
                  "ARB",
                  "VET",
                  "QNT",
                  "APE",
                  "ALGO",
                  "GRT",
                  "FTM",
                  "SAND",
                  "EOS",
                  "MANA",
                  "RPL",
                  "EGLD",
                  "THETA",
                  "AAVE"]


def stat_calc(src, lookback):
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


asset_name = 'BTC'
base_asset_name = 'USDT'
start_date = '2021-06-01'
end_date = '2023-06-02'
interval = '1d'


output = []

for asset in desired_assets:
    data = download_data(asset, base_asset_name,
                         start_date, end_date, interval)

    src = (data['High'] + data['Low'] + data['Close']) / 3

    lookback = 30

    results = stat_calc(src, lookback)
    result_d = {
        "asset": asset,
        "sharp": results[0],
        "sortino": results[1],
        "omega": results[2]
    }
    print(result_d)

    output.append(result_d)

df = pd.DataFrame(output)
df.to_csv('ratios/output/asset_metrics_rolling_risk.csv', index=False)
