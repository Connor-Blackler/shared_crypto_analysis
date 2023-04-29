from abc import ABC, abstractmethod
from enum import Enum, auto


class MarketAPIID(Enum):
    TWELVE_DATA = auto(),
    GLASSNODE = auto()


class MarketAPI(ABC):
    @abstractmethod
    def API_type(self) -> MarketAPIID:
        """Returns the MarketAPI enum that correlates to this API"""

    @abstractmethod
    def _API_URL(self) -> str:
        """Returns the URL used with this API"""

    @abstractmethod
    def _API_KEY(self) -> str:
        """Returns the API key used with this API"""

    @abstractmethod
    def _format(self) -> dict:
        """Returns the format used with this API"""

    @abstractmethod
    def _get_headers(self) -> dict:
        """Returns the header used with this API"""

    @abstractmethod
    def send_api_request(self, method: str, additional_url: str, params: dict) -> str:
        """
        Performs the API request

        method: GET, POST
        Additional_url: url added to the API_URL (/...)
        params: params to be sent to the url
        """
