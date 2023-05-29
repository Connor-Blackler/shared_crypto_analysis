import requests
from market.shared_market_provider import MarketAPIID, MarketAPI
from shared_python.shared_passwords.shared_password import PasswordRepo


class Glassnode(MarketAPI):
    def __init__(self) -> None:
        super().__init__()

        self.__API_URL = "https://api.glassnode.com/"
        self.__API_KEY = PasswordRepo().get_password_key("GLASSNODE_API_KEY")

    def API_type(self) -> MarketAPIID:
        return MarketAPIID.GLASSNODE

    def _API_URL(self) -> str:
        return self.__API_URL

    def _API_KEY(self) -> str:
        return self.__API_KEY

    def _format(self) -> dict:
        return {"timestamp_format": "unix", "api_key": self._API_KEY()}

    def _get_headers(self) -> dict:
        return {}

    def send_api_request(self, method: str, additional_url: str, params: dict) -> str:
        response = requests.request(method, self._API_URL() + additional_url,
                                    params=self._format() | params)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 403:
            return response.text.strip()
        else:
            return None
