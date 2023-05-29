from datetime import datetime
import time
import pandas as pd
from crypto_requests.request import get_price


def get_BTC_data(from_date: datetime, to_date: datetime):
    start_timestamp = int(time.mktime(from_date.timetuple()))
    end_timestamp = int(time.mktime(to_date.timetuple()))

    # Get the Bitcoin data
    data_btc = get_price("BTC", start_timestamp, end_timestamp)

    # Create a dataframe with Bitcoin data
    df_btc = pd.DataFrame(data_btc)
    df_btc['t'] = pd.to_datetime(df_btc['t'], unit='s')
    df_btc.set_index('t', inplace=True)
    df_btc.index = df_btc.index.tz_localize(None)  # make timezone-naive
    df_btc.rename(columns={'v': 'BTC'}, inplace=True)

    return df_btc
