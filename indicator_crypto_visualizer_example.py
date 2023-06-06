import pandas as pd
from custom_indicators.crypto_visualizer import get_inicator_crypto_visualizer, get_inicator_crypto_visualizer_bulk
from custom_indicators.indicator_options import OptionsVisualizer


def main() -> None:
    # Collect a single asset
    options = OptionsVisualizer(lookback=365, alpha_period=30, adr_length=14)
    data = get_inicator_crypto_visualizer("BTC", options)
    df = pd.DataFrame(data)
    df.to_csv('indicator_output/asset_metrics_crypto_visualizer.csv', index=False)

    # Collect a bulk of assets
    desired_assets = ["BTC", "ETH", "BNB", "XRP", "ADA", "DOGE", "SOL", "MATIC", "LTC", "TRX",
                      "DOT", "SHIB", "AVAX", "LINK", "ATOM", "UNI", "XMR", "XLM", "BCH", "ICP",
                      "LDO", "FIL", "APT", "HBAR", "NEAR", "ARB", "VET", "QNT", "APE", "ALGO",
                      "GRT", "FTM", "SAND", "EOS", "MANA", "RPL", "EGLD", "THETA", "AAVE"]

    options = OptionsVisualizer(lookback=365, alpha_period=30, adr_length=14)
    data = get_inicator_crypto_visualizer_bulk(desired_assets, options)
    df = pd.DataFrame(data)
    df.to_csv(
        'indicator_output/asset_metrics_crypto_visualizer_bulk.csv', index=False)


if __name__ == "__main__":
    main()
