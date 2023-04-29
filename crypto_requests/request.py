from .market.provider import MarketProviderHolder
from .indicators.provider import IndicatorsProviderHolder
from .blockchain.provider import BlockchainProviderHolder

_market_provider = MarketProviderHolder()
_indicators_provider = IndicatorsProviderHolder()
_blockchain_provider = BlockchainProviderHolder()

"""Blockchain metrics"""


def get_block_count(asset: str, start_date: int, end_date: int):
    return _blockchain_provider.get_block_count(asset, start_date, end_date)


def get_block_height(asset: str, start_date: int, end_date: int):
    return _blockchain_provider.get_block_height(asset, start_date, end_date)


def get_block_interval_mean(asset: str, start_date: int, end_date: int):
    return _blockchain_provider.get_block_interval_mean(asset, start_date, end_date)


def get_block_interval_median(asset: str, start_date: int, end_date: int):
    return _blockchain_provider.get_block_interval_median(asset, start_date, end_date)


def get_block_size_mean(asset: str, start_date: int, end_date: int):
    return _blockchain_provider.get_block_size_mean(asset, start_date, end_date)


def get_block_size_total(asset: str, start_date: int, end_date: int):
    return _blockchain_provider.get_block_size_total(asset, start_date, end_date)


"""Market metrics"""


def get_mvrv(asset: str, start_date: int, end_date: int):
    return _market_provider.get_mvrv(asset, start_date, end_date)


def get_mvrv_short_term(asset: str, start_date: int, end_date: int):
    return _market_provider.get_mvrv_short_term(asset, start_date, end_date)


def get_mvrv_long_term(asset: str, start_date: int, end_date: int):
    return _market_provider.get_mvrv_long_term(asset, start_date, end_date)


def get_mvrv_z_score(asset: str, start_date: int, end_date: int):
    """
    MVRV Z-Score is a bitcoin chart that uses blockchain analysis
    to identify periods where Bitcoin is extremely over or undervalued
    relative to its 'fair value'.
    """
    return _market_provider.get_mvrv_z_score(asset, start_date, end_date)


def get_price_drawdown(asset: str, start_date: int, end_date: int):
    return _market_provider.get_price_drawdown(asset, start_date, end_date)


def get_realized_price(asset: str, start_date: int, end_date: int):
    return _market_provider.get_realized_price(asset, start_date, end_date)


def get_realized_volatility(asset: str, start_date: int, end_date: int):
    return _market_provider.get_realized_volatility(asset, start_date, end_date)


def get_realized_volatility_1_month(asset: str, start_date: int, end_date: int):
    return _market_provider.get_realized_volatility_1_month(asset, start_date, end_date)


def get_realized_volatility_1_week(asset: str, start_date: int, end_date: int):
    return _market_provider.get_realized_volatility_1_week(asset, start_date, end_date)


def get_realized_volatility_1_year(asset: str, start_date: int, end_date: int):
    return _market_provider.get_realized_volatility_1_year(asset, start_date, end_date)


def get_realized_volatility_3_month(asset: str, start_date: int, end_date: int):
    return _market_provider.get_realized_volatility_3_month(asset, start_date, end_date)


def get_realized_volatility_6_month(asset: str, start_date: int, end_date: int):
    return _market_provider.get_realized_volatility_6_month(asset, start_date, end_date)


def get_price(asset: str, start_date: int, end_date: int):
    """The asset's closing price in USD."""
    return _market_provider.get_price(asset, start_date, end_date)


def get_market_cap(asset: str, start_date: int, end_date: int):
    """Market capitalization (or market cap) is the total dollar value of all
    the shares of a company’s stock — or, in the case of Bitcoin or another cryptocurrency,
    of all the coins that have been mined. 

    In crypto, market cap is calculated by multiplying the total number of coins
    that have been mined by the price of a single coin at any given time."""
    return _market_provider.get_market_cap(asset, start_date, end_date)


def get_realized_cap(asset: str, start_date: int, end_date: int):
    """
    Realized capitalization (realized cap) is a variation of market capitalization
    that values each UTXO based on the price when it was last moved,
    as opposed to its current value
    """
    return _market_provider.get_realized_cap(asset, start_date, end_date)


"""Indicator metrics"""


def get_mvrv_account_based(asset: str, start_date: int, end_date: int):
    """
    compares the number of transactions of a particular coin on
    a set day against that coin's market cap
    """
    return _indicators_provider.get_mvrv_account_based(asset, start_date, end_date)


def get_sopr(asset: str, start_date: int, end_date: int):
    """
    The SOPR (Spent Output Profit Ratio) indicator provides insight into macro market sentiment,
    profitability and losses taken over a particular time-frame. 
    It reflects the degree of realized profit for all coins moved on-chain.
    """
    return _indicators_provider.get_sopr(asset, start_date, end_date)


def get_entity_adjusted_nupl(asset: str, start_date: int, end_date: int):
    return _indicators_provider.get_entity_adjusted_nupl(asset, start_date, end_date)


def get_puell_multiple(asset: str, start_date: int, end_date: int):
    """
    This metric looks at the supply side of Bitcoin's economy - 
    bitcoin miners and their revenue.
    """
    return _indicators_provider.get_puell_multiple(asset, start_date, end_date)


def get_relative_unrealized_loss(asset: str, start_date: int, end_date: int):
    """
    Relative Unrealized Loss is defined as the total loss 
    in USD of all coins in existence whose price at realisation time was
    higher than the current price normalised the market cap
    """
    return _indicators_provider.get_relative_unrealized_loss(asset, start_date, end_date)


def get_relative_unrealized_profit(asset: str, start_date: int, end_date: int):
    """
    Relative unrealized profit or loss is the ratio of aggregated
    unrealized profits or loss to the market capitalization of Bitcoin
    """
    return _indicators_provider.get_relative_unrealized_profit(asset, start_date, end_date)


def get_liveliness(asset: str, start_date: int, end_date: int):
    """
    Liveliness is defined as the ratio of the sum of Coin Days
    Destroyed and the sum of all coin days ever created
    """
    return _indicators_provider.get_liveliness(asset, start_date, end_date)
