from market.market_provider import get_market_provider


def main() -> None:
    provider = get_market_provider()
    my_list = provider.get_correl("BTC", "ETH", "1week", "7")
    print(my_list.text)
