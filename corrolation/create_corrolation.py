import time
import pandas as pd
from datetime import datetime, timedelta
from statistics import mean
from .BTC_to_VIX import correlate_BTC_VIX
from .BTC_to_GOLD import correlate_BTC_GOLD
from .BTC_to_DXY import correlate_BTC_DXY
from .BTC_to_US10Y import correlate_BTC_US10Y


def main() -> None:
    start_time = time.time()
    current_date = datetime.now()
    rolling_periods = [15, 30, 60, 90, 120]
    stocks = ["DXY", "GOLD", "VIX", "US10Y"]

    # Create a DataFrame to store the correlation values
    correlation_table = pd.DataFrame(
        columns=["15D", "30D", "60D", "90D", "120D", "", "Average"])
    correlation_table = correlation_table.rename_axis('')

    dxy = []
    gold = []
    vix = []
    us10y = []

    for period in rolling_periods:
        from_date = current_date - timedelta(days=period * 2)

        correlation_dxy = correlate_BTC_DXY(from_date, current_date, period)
        correlation_table.loc['DXY', f"{period}D"] = "{:.3f}".format(
            correlation_dxy)
        dxy.append(correlation_dxy)

        correlation_gold = correlate_BTC_GOLD(from_date, current_date, period)
        correlation_table.loc['GOLD', f"{period}D"] = "{:.3f}".format(
            correlation_gold)
        gold.append(correlation_gold)

        correlation_vix = correlate_BTC_VIX(from_date, current_date, period)
        correlation_table.loc['VIX', f"{period}D"] = "{:.3f}".format(
            correlation_vix)
        vix.append(correlation_vix)

        correlation_us10y = correlate_BTC_US10Y(
            from_date, current_date, period)
        correlation_table.loc['US10Y', f"{period}D"] = "{:.3f}".format(
            correlation_us10y)
        us10y.append(correlation_us10y)

    correlation_table.loc['DXY', 'Average'] = "{:.3f}".format(mean(dxy))
    correlation_table.loc['GOLD', 'Average'] = "{:.3f}".format(mean(gold))
    correlation_table.loc['VIX', 'Average'] = "{:.3f}".format(mean(vix))
    correlation_table.loc['US10Y', 'Average'] = "{:.3f}".format(mean(us10y))

    # Save the correlation table to a CSV file
    correlation_table.to_csv('./corrolation/output/btc_correlation.csv')

    # Save the image DataFrame to a separate sheet in the CSV file
    with pd.ExcelWriter('./corrolation/output/btc_correlation.xlsx') as writer:
        info_table = pd.DataFrame(columns=[""])
        info_table = info_table.rename_axis('')

        info_table.loc['', ''] = 'Generated by Confiend with Python. Source code: Available on request'
        info_table.to_excel(writer, sheet_name='Correlation Table',
                            index=True, startrow=1, startcol=1)

        info_table.loc['', ''] = f"Total time taken to generate: " + \
            ("--- %s seconds ---" % (time.time() - start_time))
        info_table.to_excel(writer, sheet_name='Correlation Table',
                            index=True, startrow=2, startcol=1)

        correlation_table.to_excel(
            writer, sheet_name='Correlation Table', index=True, startrow=5, startcol=2)

        for period in rolling_periods:
            for stock in stocks:
                sheet_name = f'{stock} ({period}D)'
                image_table = pd.DataFrame(
                    {f'{stock} ({period}D)': [f'{stock}_rolling_correlation_plot_{period}.png']})
                image_table.to_excel(
                    writer, sheet_name=sheet_name, index=False)


if __name__ == "__main__":
    main()
