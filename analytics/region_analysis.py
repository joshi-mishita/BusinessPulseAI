import pandas as pd

def get_region_profit(df):

    region_profit = (
        df.groupby("Region")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    return region_profit