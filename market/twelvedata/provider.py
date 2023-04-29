import requests
from market.shared_market_provider import MarketAPIID, MarketAPI
from shared_python.shared_passwords.shared_password import passwords_repo


class TwelveData(MarketAPI):
    def __init__(self) -> None:
        super().__init__()

        self.__API_KEY = passwords_repo().get_password_key("TWELVE_DATA_API_KEY")
        self.__API_URL = "https://twelve-data1.p.rapidapi.com/"

    def API_type(self) -> MarketAPIID:
        return MarketAPIID.TWELVE_DATA

    def _API_URL(self) -> str:
        return self.__API_URL

    def _API_KEY(self) -> str:
        return self.__API_KEY

    def _format(self) -> dict:
        return {"format": "json"}

    def _get_headers(self) -> dict:
        return {
            "X-RapidAPI-Key": self._API_KEY(),
            "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
        }

    def send_api_request(self, method: str, additional_url: str, params: dict) -> str:
        return requests.request(method, self._API_URL + additional_url,
                                headers=self._get_headers(), params=self._format() | params)

    def get_list(self) -> str:
        """Returns a dictionary of all crypto on the market"""
        return self.send_api_request("GET", "cryptocurrencies", {})

    def get_specific(self, coin: str) -> str:
        """
        returns a dictionary of a specific crypto
        coin: BTC -> (Bitcoin) / ETH (Ethereum)
        """
        return self.send_api_request("GET", "cryptocurrencies", {"currency_base": coin})

    def get_correl(self, symbol_a: str, symbol_b: str, interval: str, duration: str) -> str:
        additional_params = {
            "symbol": f"{symbol_a}/{symbol_b}",
            "interval": interval,
            "time_period": duration,
            "series_type_1": "open",
            "series_type_2": "close",
            "outputsize": "30"
        }

        return self.send_api_request("GET", "correl", additional_params)
