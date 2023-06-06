"""
Certainly! The Aroon indicator is a technical analysis tool used to identify the 
strength and direction of a trend as well as potential trend reversals. 
It consists of two lines: the Aroon Up line and the Aroon Down line.

The Aroon Up line measures the number of periods since the highest high within a given 
lookback period. It indicates how many periods have passed since the most recent high point. 
A higher value of the Aroon Up suggests a stronger upward trend.

The Aroon Down line, on the other hand, measures the number of periods since the 
lowest low within the same lookback period. It indicates how many periods have passed 
since the most recent low point. A higher value of the Aroon Down suggests a stronger downward trend.
"""

from datetime import datetime
from crypto_requests.request import get_historical_klines


def calculate_aroon(asset: str, length: int = 14, quote_name: str = "USDT",
                    start_date: str = "2010-01-01", end_date: str = datetime.today().strftime('%Y-%m-%d'),
                    interval: str = "1d"):
    data = get_historical_klines(
        asset, quote_name, start_date, end_date, interval)
    high = data['High'].tolist()
    low = data['Low'].tolist()

    # Calculate highest high
    last_highs = high[-length:]
    highest_high = max(last_highs)
    highest_index = len(high) - high.index(highest_high) - 1

    # Calculate lowest low
    last_lows = low[-length:]
    lowest_low = min(last_lows)
    lowest_index = len(low) - low.index(lowest_low) - 1

    # Calculate Aroon Up and Aroon Down
    aroon_up = 100 * (length - highest_index) / length
    aroon_down = 100 * (length - lowest_index) / length

    return aroon_up, aroon_down


asset = 'ETH'
aroon_up, aroon_down = calculate_aroon(asset)
print("Aroon Up:", aroon_up)
print("Aroon Down:", aroon_down)
