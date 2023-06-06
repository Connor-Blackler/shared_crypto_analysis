from abc import ABC, abstractmethod
from enum import Enum, auto


class MarketAPIID(Enum):
    TWELVE_DATA = auto(),
    GLASSNODE = auto(),
    BINANCE = auto()


class MarketAPI(ABC):
    @abstractmethod
    def API_type(self) -> MarketAPIID:
        """Returns the MarketAPI enum that correlates to this API"""
