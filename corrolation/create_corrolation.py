import requests
import time
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import yfinance as yf
from pprint import pprint
import mplcursors

from crypto_requests.request import get_price


def _get_DXY_data(from_date: datetime, to_date: datetime):
    # Get a common date index which includes all the days (including weekends)
    start_time_str = from_date.strftime('%Y-%m-%d')
    end_date_str = to_date.strftime('%Y-%m-%d')

    # Get DXY data using yfinance
    dxy = yf.Ticker("DX-Y.NYB")
    df_dxy = dxy.history(start=start_time_str, end=end_date_str)
    df_dxy = df_dxy[['Close']]

    return df_dxy


def _get_BTC_data(from_date: datetime, to_date: datetime):
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


def _populate_BTC_DXY(from_date: datetime, to_date: datetime, rolling_amount: int, show: bool = False) -> float:
    df_btc = _get_BTC_data(from_date, to_date)
    df_dxy = _get_DXY_data(from_date, to_date)

    # Make both indexes timezone-naive
    start_time_str = from_date.strftime('%Y-%m-%d')
    end_date_str = to_date.strftime('%Y-%m-%d')
    common_dates = pd.date_range(
        start=start_time_str, end=end_date_str)

    common_dates = common_dates.tz_localize(None)
    df_dxy.index = df_dxy.index.tz_localize(None)

    df_dxy = df_dxy.reindex(common_dates, method='ffill')
    df_btc = df_btc.reindex(common_dates).ffill()

    # Calculate rolling correlations for different time periods
    rolling_correlation = df_btc['BTC'].rolling(
        window=rolling_amount).corr(df_dxy['Close'])

    if show:
        # Print rolling correlation
        print("\nRolling Correlation:")
        print(rolling_correlation)
        # Plot the rolling correlation
        plt.figure(figsize=(12, 6))
        plt.plot(common_dates.strftime('%m/%d'), rolling_correlation)
        plt.title(
            f'{rolling_amount} day Rolling Correlation between BTC and DXY, Made by Confiend, generated with APIs')
        plt.xlabel('Date')
        plt.ylabel('Correlation')
        plt.ylim(-1, 1)  # Set y-axis limits to -1 and 1
        plt.xticks(rotation='vertical')  # Rotate x-axis labels vertically
        plt.yticks(np.arange(-1, 1.1, 0.1))  # Set y-axis tick interval to 0.1
        plt.grid(True)

        # Add annotation labels to the plot for hover display
        cursor = mplcursors.cursor(hover=True)
        cursor.connect("add", lambda sel: sel.annotation.set_text(
            f"Correlation: {sel.target[1]:.2f}"))

        plt.show()

    return rolling_correlation.iloc[-1]


def main() -> None:
    current_date = datetime.now()
    from_date = current_date - timedelta(days=60)

    print("15 day correl: ", _populate_BTC_DXY(
        current_date - timedelta(days=30), current_date, 15))
    print("30 day correl: ", _populate_BTC_DXY(
        current_date - timedelta(days=60), current_date, 30))
    print("60 day correl: ", _populate_BTC_DXY(
        current_date - timedelta(days=120), current_date, 60))
    print("120 day correl: ", _populate_BTC_DXY(
        current_date - timedelta(days=240), current_date, 120))


if __name__ == "__main__":
    main()
