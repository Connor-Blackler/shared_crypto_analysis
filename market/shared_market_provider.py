from abc import ABC, abstractmethod
from enum import Enum, auto


class MarketAPI(Enum):
    TWELVE_DATA = auto()


class MarketProvider(ABC):
    @abstractmethod
    def get_list(self) -> dict:
        """Returns a dictionary of all crypto lists provided by the API"""

    @abstractmethod
    def get_specific(self, coin: str) -> dict:
        """returns a dictionary of a specific crypto"""

    @abstractmethod
    def get_correl(self, symbol_a: str, symbol_b: str, interval: str, duration: str) -> dict:
        """
        returns the correl between:
        symbol_a = ETH
        symbol_b = USD
        duration = 1min / 1h / 1day / 1week / 1month
        """
