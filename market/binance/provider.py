import os
from binance import *
from market.shared_market_provider import MarketAPIID, MarketAPI


class Binance(MarketAPI):
    def __init__(self) -> None:
        super().__init__()

        self._client = Client(os.getenv('BINANCE_KEY'),
                              os.getenv('BINANCE_SECRET'))

    def API_type(self) -> MarketAPIID:
        return MarketAPIID.BINANCE

    def client(self) -> Client:
        return self._client
