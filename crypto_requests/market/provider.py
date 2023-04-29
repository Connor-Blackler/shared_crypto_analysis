from crypto_requests.market.glassnode import GlassnodeMarket
from crypto_requests.market.twlevedata import TwelveDataMarket


class MarketProviderHolder():
    def __init__(self) -> None:

        self._glassnode = GlassnodeMarket()
        self.__glassnode_methods = [f for f in dir(
            GlassnodeMarket) if not f.startswith('_')]

        self._twelvedata = TwelveDataMarket()
        self.__twlevedata_methods = [f for f in dir(
            TwelveDataMarket) if not f.startswith('_')]

    def __getattr__(self, func):
        """Delegate calls to the API if the API has the method"""
        def method(*args, **kwargs):
            if func in self.__glassnode_methods:
                return getattr(self._glassnode, func)(*args, **kwargs)

            elif func in self.__twlevedata_methods:
                return getattr(self._twelvedata, func)(*args, **kwargs)

            else:
                raise AttributeError

        return method
