from .glassnode import GlassnodeMarket
from .twelvedata import TwelveDataMarket
from .binance import BinanceMarket


class MarketProviderHolder():
    def __init__(self) -> None:

        self._glassnode = GlassnodeMarket()
        self.__glassnode_methods = [f for f in dir(
            GlassnodeMarket) if not f.startswith('_')]

        self._twelvedata = TwelveDataMarket()
        self.__twelvedata_methods = [f for f in dir(
            TwelveDataMarket) if not f.startswith('_')]

        self._binance = BinanceMarket()
        self.__binance_methods = [f for f in dir(
            BinanceMarket) if not f.startswith('_')]

    def __getattr__(self, func):
        """Delegate calls to the API if the API has the method"""
        def method(*args, **kwargs):
            if func in self.__glassnode_methods:
                return getattr(self._glassnode, func)(*args, **kwargs)

            elif func in self.__twelvedata_methods:
                return getattr(self._twelvedata, func)(*args, **kwargs)

            elif func in self.__binance_methods:
                return getattr(self._binance, func)(*args, **kwargs)

            else:
                raise AttributeError

        return method
