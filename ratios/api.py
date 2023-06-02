import pandas as pd
import requests


def download_data_cryptocompare(asset_name: str, base_asset_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    url = "https://min-api.cryptocompare.com/data/v2/histoday"
    interval = pd.Timedelta(days=200)  # Split interval into chunks of 200 days

    dataframes = []

    while start_date < end_date:
        # Determine the end date for the current interval
        interval_end_date = min(pd.Timestamp(
            start_date) + interval, pd.Timestamp(end_date))

        # Format the API request parameters
        params = {
            "fsym": asset_name,
            "tsym": base_asset_name,
            "toTs": interval_end_date.timestamp(),
            "limit": (interval_end_date - pd.Timestamp(start_date)).days + 1
        }

        # Send the API request
        response = requests.get(url, params=params)
        data = response.json()

        # Process the response data
        if data["Response"] == "Success":
            df = pd.DataFrame(data["Data"]["Data"])
            df["time"] = pd.to_datetime(df["time"], unit="s")
            df = df.rename(columns={"time": "Timestamp"})
            df = df.set_index("Timestamp")
            df = df[["open", "high", "low", "close",
                     "volumefrom", "volumeto"]]
            df.columns = ["Open", "High", "Low", "Close",
                          "Volume", "Quote Asset Volume"]
            dataframes.append(df)

        # Update the start date for the next interval
        start_date = (interval_end_date + pd.Timedelta(days=1)
                      ).strftime("%Y-%m-%d")

    if dataframes:
        return pd.concat(dataframes)

    return None


def main():
    # Example usage
    asset_name = 'BTC'
    base_asset_name = 'USDT'
    start_date = '2010-08-17'
    end_date = '2023-06-02'

    # Using CryptoCompare API
    data_cryptocompare = download_data_cryptocompare(
        asset_name, base_asset_name, start_date, end_date)
    print(data_cryptocompare)
