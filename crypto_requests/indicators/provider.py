from .glassnode import GlassnodeIndicator
from .twelvedata import TwelveDataIndicator
from .binance import BinanceIndicator


class IndicatorsProviderHolder():
    def __init__(self) -> None:

        self._glassnode = GlassnodeIndicator()
        self.__glassnode_methods = [f for f in dir(
            GlassnodeIndicator) if not f.startswith('_')]

        self._twelvedata = TwelveDataIndicator()
        self.__twelvedata_methods = [f for f in dir(
            TwelveDataIndicator) if not f.startswith('_')]

        self._binancedata = BinanceIndicator()
        self.___binancedata_methods = [f for f in dir(
            BinanceIndicator) if not f.startswith('_')]

    def __getattr__(self, func):
        """Delegate calls to the API if the API has the method"""
        def method(*args, **kwargs):
            if func in self.__glassnode_methods:
                return getattr(self._glassnode, func)(*args, **kwargs)

            elif func in self.__twelvedata_methods:
                return getattr(self._twelvedata, func)(*args, **kwargs)

            elif func in self.___binancedata_methods:
                return getattr(self._binancedata, func)(*args, **kwargs)

            else:
                raise AttributeError

        return method
