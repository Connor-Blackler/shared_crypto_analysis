"""
Puell uses miner revenue instead of just coin issuance to calculate the multiple.
Puell Multiple = Mining Revenue / (365-day moving average of Mining Revenue)
"""

from datetime import datetime
import os
import quandl

quandl.ApiConfig.api_key = os.getenv('QUANDL_API_KEY')


def get_puell_multiple(start_date: str = "2021-06-01", end_date: str = datetime.today().strftime('%Y-%m-%d')):
    miningRevenue_df = quandl.get(
        "BCHAIN/MIREV", start_date=start_date, end_date=end_date)

    miningRevenue_df['MA365'] = miningRevenue_df['Value'].rolling(
        window=365).mean()
    miningRevenue_df['PuellMultiple'] = miningRevenue_df['Value'] / \
        miningRevenue_df['MA365']

    miningRevenue_df['PuellMultiple'] = miningRevenue_df['PuellMultiple'].shift(
        1)

    return miningRevenue_df


if __name__ == "__main__":
    print(get_puell_multiple())
