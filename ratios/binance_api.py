import os
from binance import *
import pandas as pd

# Replace with your Binance API credentials
api_key = os.getenv('BINANCE_KEY')
api_secret = os.getenv('BINANCE_SECRET')
"""
go to https://binance-docs.github.io/apidocs/spot/en/#introduction
create a new api key-secret (top option of the two)
on windows, add as an environment variable:
- search -> "edit the system environment variables"
- click "environment variables" at the bottom right
- on the top section, click the "new"
- name: BINANCE_KEY
- value: [you api key from binance site]
- click ok
- on the top section, click the "new"
- name: BINANCE_SECRET
- value: [you api secret from binance site]
- click ok
- click ok
- click ok
- may have to restart visual studio code if you are using it are you Python IDE
"""


def download_data(asset_name: str, base_asset_name: str, start_date: str, end_date: str, interval: str) -> pd.DataFrame:
    client = Client(api_key, api_secret)
    klines = client.get_historical_klines(
        asset_name + base_asset_name, interval, start_date, end_date)

    df = pd.DataFrame(klines, columns=["Timestamp", "Open", "High", "Low", "Close", "Volume", "Close Time",
                                       "Quote Asset Volume", "Number of Trades", "Taker Buy Base Asset Volume",
                                       "Taker Buy Quote Asset Volume", "Ignore"])

    df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit='ms')
    df = df.set_index("Timestamp")
    df = df.astype(float)

    return df
