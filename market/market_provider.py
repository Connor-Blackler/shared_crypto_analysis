from .shared_market_provider import MarketAPI
from .twelvedata.provider import TwelveData
from .glassnode.provider import Glassnode
from .binance.provider import Binance

_apis = [
    TwelveData(),
    Glassnode(),
    Binance()
]


def get_apis() -> list[MarketAPI]:
    return _apis
