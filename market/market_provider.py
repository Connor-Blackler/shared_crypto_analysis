from .shared_market_provider import MarketAPI
from .twelvedata.provider import TwelveData
from .glassnode.provider import Glassnode

_apis = [
    TwelveData(),
    Glassnode()
]


def get_apis() -> list[MarketAPI]:
    return _apis
