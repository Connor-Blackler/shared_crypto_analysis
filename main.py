from indicator_crypto_visualizer_example import main as crypto_visualizer
from indicator_rolling_risk_example import main as rolling_risk
from crypto_requests.request import *
import time
import datetime
from corrolation.create_corrolation import main
import custom_indicators.aroon
exit()


rolling_risk()
crypto_visualizer()

exit()

asset = "BTC"
start_date = "2022-01-15"
end_date = "2021-02-15"

start_date = int(time.mktime(datetime.datetime(2023, 1, 15).timetuple()))
end_date = int(time.mktime(datetime.datetime(2023, 2, 15).timetuple()))

"""Blockchain calls"""
print(get_block_count(asset, start_date, end_date))
print(get_block_height(asset, start_date, end_date))
print(get_block_interval_mean(asset, start_date, end_date))
print(get_block_interval_median(asset, start_date, end_date))
print(get_block_size_mean(asset, start_date, end_date))
print(get_block_size_total(asset, start_date, end_date))

"""Market calls"""

print(get_mvrv(asset, start_date, end_date))
print(get_mvrv_short_term(asset, start_date, end_date))
print(get_mvrv_long_term(asset, start_date, end_date))
print(get_mvrv_z_score(asset, start_date, end_date))
print(get_price_drawdown(asset, start_date, end_date))
print(get_realized_price(asset, start_date, end_date))
print(get_realized_volatility(asset, start_date, end_date))
print(get_realized_volatility_1_month(asset, start_date, end_date))
print(get_realized_volatility_1_week(asset, start_date, end_date))
print(get_realized_volatility_1_year(asset, start_date, end_date))
print(get_realized_volatility_3_month(asset, start_date, end_date))
print(get_realized_volatility_6_month(asset, start_date, end_date))
print(get_price(asset, start_date, end_date))
print(get_market_cap(asset, start_date, end_date))
print(get_realized_cap(asset, start_date, end_date))

"""indicator calls"""
print(get_mvrv_account_based(asset, start_date, end_date))
print(get_sopr(asset, start_date, end_date))
print(get_entity_adjusted_nupl(asset, start_date, end_date))
print(get_puell_multiple(asset, start_date, end_date))
print(get_relative_unrealized_profit(asset, start_date, end_date))
print(get_liveliness(asset, start_date, end_date))
