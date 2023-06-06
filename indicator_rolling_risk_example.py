import pandas as pd
from custom_indicators.rolling_risk import get_inicator_rolling_risk
from custom_indicators.indicator_options import OptionsRollingRisk


def main() -> None:
    desired_assets = ["BTC", "ETH", "BNB", "XRP", "ADA", "DOGE", "SOL", "MATIC", "LTC", "TRX",
                      "DOT", "SHIB", "AVAX", "LINK", "ATOM", "UNI", "XMR", "XLM", "BCH", "ICP",
                      "LDO", "FIL", "APT", "HBAR", "NEAR", "ARB", "VET", "QNT", "APE", "ALGO",
                      "GRT", "FTM", "SAND", "EOS", "MANA", "RPL", "EGLD", "THETA", "AAVE"]

    options = OptionsRollingRisk(lookback=30)
    data = get_inicator_rolling_risk(desired_assets, options)
    df = pd.DataFrame(data)
    df.to_csv('indicator_output/asset_metrics_rolling_risk.csv', index=False)


if __name__ == "__main__":
    main()
