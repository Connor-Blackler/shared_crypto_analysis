from datetime import datetime
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import mplcursors
import numpy as np

from .BTC import get_BTC_data


def _get_DXY_data(from_date: datetime, to_date: datetime):
    # Get a common date index which includes all the days (including weekends)
    start_time_str = from_date.strftime('%Y-%m-%d')
    end_date_str = to_date.strftime('%Y-%m-%d')

    # Get DXY data using yfinance
    dxy = yf.Ticker("DX-Y.NYB")
    df_dxy = dxy.history(start=start_time_str, end=end_date_str)
    df_dxy = df_dxy[['Close']]

    return df_dxy


def correlate_BTC_DXY(from_date: datetime, to_date: datetime, rolling_amount: int) -> float:
    df_btc = get_BTC_data(from_date, to_date)
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

    plt.figure(figsize=(12, 6))
    plt.plot(common_dates.strftime('%m/%d'), rolling_correlation)
    plt.title(
        f'{rolling_amount} day Rolling Correlation between BTC and DXY, Made by Confiend, Automatically generated with APIs')
    plt.xlabel('Date')
    plt.ylabel('Correlation')
    plt.ylim(-1, 1)  # Set y-axis limits to -1 and 1
    plt.xticks(rotation='vertical')  # Rotate x-axis labels vertically
    plt.yticks(np.arange(-1, 1.1, 0.1))  # Set y-axis tick interval to 0.1
    plt.grid(True)

    # Save the image of the plot to desktop
    plt.savefig(
        f'./corrolation/output/DXY_rolling_correlation_plot_{rolling_amount}.png')

    # Add annotation labels to the plot for hover display
    cursor = mplcursors.cursor(hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(
        f"Correlation: {sel.target[1]:.2f}"))

    return rolling_correlation.iloc[-1]
