from collections import defaultdict
from datetime import datetime
import pandas as pd
import numpy as np
from crypto_requests.request import get_historical_klines
from .indicator_options import OptionsVisualizer


class _AssetCalc:
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
            f"athdd: {self.athdd.tail(1).values[0]:.0%}\n"
            f"adr: {self.adr:.2%}\n"
        )

    def f_beta(self) -> float:
        daily_return = self.src / self.src.shift(1) - 1
        daily_return.iloc[0] = 0  # first day of data, avoid NaN

        daily_base_return = self.base / self.base.shift(1) - 1
        daily_base_return.iloc[0] = 0  # first day of data, avoid NaN

        returns_array = []
        returns_base_array = []

        for i in range(len(returns_array) - 1, len(returns_array) - self.lookback - 2, -1):
            returns_array.append(daily_return[i])
            returns_base_array.append(daily_base_return[i])

        return np.cov(returns_array, returns_base_array)[0, 1] / np.var(returns_base_array)

    def f_alpha(self) -> float:
        daily_return = self.src / self.src.shift(1) - 1
        daily_return.iloc[0] = 0  # first day of data, avoid NaN

        daily_base_return = self.base / self.base.shift(1) - 1
        daily_base_return.iloc[0] = 0  # first day of data, avoid NaN

        returns_array = []
        returns_base_array = []

        for i in range(len(returns_array) - 1, len(returns_array) - self.alpha_period - 2, -1):
            returns_array.append(daily_return[i])
            returns_base_array.append(daily_base_return[i])

        return sum(returns_array) - sum(returns_base_array) * self.f_beta()

    def f_sharpe(self) -> float:
        daily_return = self.src / self.src.shift(1) - 1
        daily_return.iloc[0] = 0  # first day of data, avoid NaN

        returns_array = []

        for i in range(len(returns_array) - 1, len(returns_array) - self.lookback - 2, -1):
            returns_array.append(daily_return[i])

        # STAT CALCULATIONS
        standard_deviation = np.std(returns_array)
        mean = np.mean(returns_array)
        sharpe = round(mean / standard_deviation * np.sqrt(self.lookback), 2)

        return sharpe

    def f_sortino(self) -> float:
        daily_return = self.src / self.src.shift(1) - 1
        daily_return.iloc[0] = 0  # first day of data, avoid NaN

        returns_array = []
        negative_returns_array = []

        for i in range(len(returns_array) - 1, len(returns_array) - self.lookback - 2, -1):
            returns_array.append(daily_return[i])
            if daily_return[i] <= 0.0:
                negative_returns_array.append(daily_return[i])

        # STAT CALCULATIONS
        negative_returns_standard_deviation = np.std(negative_returns_array)
        mean = np.mean(returns_array)
        sortino = round(
            mean / negative_returns_standard_deviation * np.sqrt(self.lookback), 2)

        return sortino

    def f_omega(self) -> float:
        daily_return = self.src / self.src.shift(1) - 1
        daily_return.iloc[0] = 0  # first day of data, avoid NaN

        negative_returns_array = []
        positive_returns_array = []

        for i in range(len(daily_return) - 1, len(daily_return) - self.lookback - 2, -1):
            if daily_return[i] <= 0.0:
                negative_returns_array.append(daily_return[i])
            else:
                positive_returns_array.append(daily_return[i])

        positive_area = sum(positive_returns_array)
        negative_area = sum(negative_returns_array) * (-1)
        omega = round(positive_area / negative_area, 2)

        return omega

    def f_zscore(self) -> pd.Series:
        sma = self.src.rolling(window=self.lookback).mean()
        stdev = self.src.rolling(window=self.lookback).std()
        return (self.src - sma) / stdev

    def f_ath_dd(self) -> pd.Series:
        ath = self.src.cummax()
        return (self.src / ath) - 1

    def f_ADR(self) -> float:
        adr = (self.high / self.low).rolling(window=self.adr_length).mean()
        return adr.iloc[-1] - 1


def get_inicator_crypto_visualizer_bulk(assets: list[str], options: OptionsVisualizer = OptionsVisualizer(),
                                        quote_name: str = "USDT", start_date: str = "2010-01-01",
                                        end_date: str = datetime.today().strftime('%Y-%m-%d'), interval: str = "1d"):
    base_data = get_historical_klines("BTC",
                                      quote_name,
                                      start_date,
                                      end_date,
                                      interval)
    data_dict = defaultdict(list)

    for asset_name in assets:
        data = get_historical_klines(asset_name,
                                     quote_name,
                                     start_date,
                                     end_date,
                                     interval)

        src_data_hlc3 = (data['High'] + data['Low'] + data['Close']) / 3
        base_data_hlc3 = (base_data['High'] +
                          base_data['Low'] + base_data['Close']) / 3

        lookback = min(options.lookback, len(src_data_hlc3) - 1)
        asset_obj = _AssetCalc(name=asset_name, src=src_data_hlc3, base=base_data_hlc3, high=data['High'], low=data['Low'],
                               lookback=lookback, alpha_period=options.alpha_period, adr_length=options.adr_length)

        data_dict["Asset"].append(asset_obj.name)
        data_dict["Beta"].append(f"{asset_obj.beta:.2f}")
        data_dict["Alpha"].append(f"{asset_obj.alpha:.2f}")
        data_dict["Sharpe"].append(f"{asset_obj.sharpe:.2f}")
        data_dict["Sortino"].append(f"{asset_obj.sortino:.2f}")
        data_dict["Omega"].append(f"{asset_obj.omega:.2f}")
        data_dict["ZScore"].append(f"{asset_obj.zscore.tail(1).values[0]:.2f}")
        data_dict["ATHDD"].append(f"{asset_obj.athdd.tail(1).values[0]:.0%}")
        data_dict["ADR"].append(f"{asset_obj.adr:.2%}")

    return data_dict


def get_inicator_crypto_visualizer(asset_name: str, options: OptionsVisualizer = OptionsVisualizer(),
                                   quote_name: str = "USDT", start_date: str = "2010-01-01",
                                   end_date: str = datetime.today().strftime('%Y-%m-%d'), interval: str = "1d"):

    return get_inicator_crypto_visualizer_bulk([asset_name], options, quote_name, start_date, end_date, interval)
