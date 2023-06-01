import pandas as pd
import numpy as np
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
                  "FIL",  # "APT",
                  "HBAR",
                  "NEAR",  # "ARB",
                  "VET",
                  "QNT",
                  "APE",
                  "ALGO",
                  "GRT",
                  "FTM",
                  "SAND",
                  "EOS",
                  "MANA",  # "RPL",
                  "EGLD",
                  "THETA",
                  "AAVE"]


class Asset:
    def __init__(self, name: str, src: pd.Series, base: pd.Series, high: pd.Series, low: pd.Series,
                 lookback: int, alpha_period: int, adr_length: int):
        """
        name (str): The name of the asset.
        src (pd.Series): The data for the source calculation.
        base (pd.Series): The base asset for comparison.
        high (pd.Series): The highest prices in each period.
        low (pd.Series): The lowest prices in each period.
        lookback (int): The length of lookback periods.
        alpha_period (int): The period for calculating alpha.
        adr_length (int): The length of Average Daily Range calculation period.
        """
        self.name = name
        self.src = src
        self.base = base
        self.high = high
        self.low = low
        self.lookback = lookback
        self.alpha_period = alpha_period
        self.adr_length = adr_length
        # Calculate metrics.
        self.beta = self.f_beta()
        self.alpha = self.f_alpha()
        self.sharpe = self.f_sharpe()
        self.sortino = self.f_sortino()
        self.omega = self.f_omega()
        self.zscore = self.f_zscore()
        self.athdd = self.f_ath_dd()
        self.adr = self.f_ADR()

    def __str__(self) -> str:
        return (
            f"asset: {self.name}\n"
            f"beta: {self.beta:.2f}\n"
            f"alpha: {self.alpha:.2f}\n"
            f"sharpe: {self.sharpe:.2f}\n"
            f"sortino: {self.sortino:.2f}\n"
            f"omega: {self.omega:.2f}\n"
            f"zscore: {self.zscore.tail(1).values[0]:.2f}\n"
            f"athdd: {self.athdd.tail(1).values[0]:.2%}\n"
            f"adr: {self.adr:.2%}\n"
        )

    def f_beta(self) -> float:
        daily_return = self.src / self.src.shift(1) - 1
        daily_base_return = self.base / self.base.shift(1) - 1
        returns_array = daily_return.tail(self.lookback)
        returns_base_array = daily_base_return.tail(self.lookback)
        return np.cov(returns_array, returns_base_array)[0, 1] / np.var(returns_base_array)

    def f_alpha(self) -> float:
        daily_return = self.src / self.src.shift(1) - 1
        daily_base_return = self.base / self.base.shift(1) - 1
        returns_array = daily_return.tail(self.alpha_period)
        returns_base_array = daily_base_return.tail(self.alpha_period)
        return returns_array.sum() - returns_base_array.sum() * self.f_beta()

    def f_sharpe(self) -> float:
        daily_return = self.src / self.src.shift(1) - 1
        returns_array = daily_return.tail(self.lookback)
        standard_deviation = returns_array.std()
        mean = returns_array.mean()
        return round(mean / standard_deviation * np.sqrt(self.lookback), 2)

    def f_sortino(self) -> float:
        daily_return = self.src / self.src.shift(1) - 1
        returns_array = daily_return.tail(self.lookback)
        negative_returns_array = returns_array[returns_array <= 0]
        negative_returns_standard_deviation = negative_returns_array.std()
        mean = returns_array.mean()
        return round(mean / negative_returns_standard_deviation * np.sqrt(self.lookback), 2)

    def f_omega(self) -> float:
        daily_return = self.src / self.src.shift(1) - 1
        negative_returns_array = daily_return[daily_return <= 0]
        positive_returns_array = daily_return[daily_return > 0]
        positive_area = positive_returns_array.sum()
        negative_area = negative_returns_array.sum() * (-1)
        return round(positive_area / negative_area, 2)

    def f_zscore(self) -> pd.Series:
        sma = self.src.rolling(window=self.lookback).mean()
        stdev = self.src.rolling(window=self.lookback).std()
        return (self.src - sma) / stdev

    def f_ath_dd(self) -> pd.Series:
        ath = self.src.max()
        return self.src / ath - 1

    def f_ADR(self) -> float:
        return (self.high / self.low).tail(self.lookback).mean() - 1


asset_name = 'BTC'
base_asset_name = 'USDT'
start_date = '2021-06-01'
end_date = '2023-06-01'
interval = '1d'

base_data = download_data(
    asset_name, base_asset_name, start_date, end_date, interval)

assets = []

for asset in ["BTC"]:
    data = download_data(asset, base_asset_name,
                         start_date, end_date, interval)

    # Adjust the 'src' calculation to hlc3
    src_data = (data['High'] + data['Low'] + data['Close']) / 3
    base_data_hlc3 = (base_data['High'] +
                      base_data['Low'] + base_data['Close']) / 3

    asset_obj = Asset(name=asset, src=src_data, base=base_data_hlc3, high=data['High'], low=data['Low'],
                      lookback=365, alpha_period=30, adr_length=14)

    print(asset_obj)
    assets.append(asset_obj)

data_dict = {
    "Asset": [asset.name for asset in assets],
    "Beta": [f"{asset.beta:.2f}" for asset in assets],
    "Alpha": [f"{asset.alpha:.2f}" for asset in assets],
    "Sharpe": [f"{asset.sharpe:.2f}" for asset in assets],
    "Sortino": [f"{asset.sortino:.2f}" for asset in assets],
    "Omega": [f"{asset.omega:.2f}" for asset in assets],
    "ZScore": [f"{asset.zscore.tail(1).values[0]:.2f}" for asset in assets],
    "ATHDD": [f"{asset.athdd.tail(1).values[0]:.2%}" for asset in assets],
    "ADR": [f"{asset.adr:.2%}" for asset in assets]
}
df = pd.DataFrame(data_dict)
df.to_csv('asset_metrics.csv', index=False)
