import requests
from market.shared_market_provider import MarketAPIID, MarketAPI
from shared_python.shared_passwords.shared_password import PasswordRepo


class TwelveData(MarketAPI):
    def __init__(self) -> None:
        super().__init__()

        self.__API_KEY = PasswordRepo().get_password_key("TWELVE_DATA_API_KEY")
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
