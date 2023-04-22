from .shared_market_provider import MarketAPI, MarketProvider
from .twelvedata.provider import TwelveData


def _apis() -> list[MarketAPI]:
    return [
        TwelveData(),
    ]


def get_market_provider(api: MarketAPI = MarketAPI.TWELVE_DATA) -> MarketProvider:
    for provider in _apis():
        if provider.api() == api:
            return provider
