import pandas as pd
from market.binance.provider import Binance


class BinanceMarket(Binance):
    def get_historical_klines(self, asset_name: str, base_asset_name: str, start_date: str, end_date: str, interval: str) -> pd.DataFrame:
        klines = self.client().get_historical_klines(
            asset_name + base_asset_name, interval, start_date, end_date)

        df = pd.DataFrame(klines, columns=["Timestamp", "Open", "High", "Low", "Close", "Volume", "Close Time",
                                           "Quote Asset Volume", "Number of Trades", "Taker Buy Base Asset Volume",
                                           "Taker Buy Quote Asset Volume", "Ignore"])

        df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit='ms')
        df = df.set_index("Timestamp")
        df = df.astype(float)

        return df
