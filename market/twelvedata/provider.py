import requests
from market.shared_market_provider import MarketProvider, MarketAPI
from .get_api_key import TwelveDataAPIKey

_api_key = TwelveDataAPIKey().get_api_key()


class TwelveData(MarketProvider):
    def __init__(self) -> None:
        super().__init__()

        self._API_URL = "https://twelve-data1.p.rapidapi.com"

    def api(self) -> MarketAPI:
        return MarketAPI.TWELVE_DATA

    def _format(self) -> dict:
        return {"format": "json"}

    def _get_headers(self) -> dict:
        return {
            "X-RapidAPI-Key": _api_key,
            "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
        }

    def get_list(self) -> dict:
        """Returns a dictionary of all crypto on the market"""
        return requests.request("GET", self._API_URL + "/cryptocurrencies", headers=self._get_headers(), params=self._format())

    def get_specific(self, coin: str) -> dict:
        """
        returns a dictionary of a specific crypto
        coin: BTC -> (Bitcoin) / ETH (Ethereum)
        """
        return requests.request("GET", self._API_URL + "/cryptocurrencies",
                                headers=self._get_headers(),
                                params=self._format() | {"currency_base": coin})

    def get_correl(self, symbol_a: str, symbol_b: str, interval: str, duration: str) -> dict:
        additional_params = {
            "symbol": f"{symbol_a}/{symbol_b}",
            "interval": interval,
            "time_period": duration,
            "series_type_1": "open",
            "series_type_2": "close",
            "outputsize": "30"
        }

        return requests.request("GET", self._API_URL + "/correl",
                                headers=self._get_headers(),
                                params=self._format() | additional_params)
