import pandas as pd

def get_category_profit(df):

    category_profit = (
        df.groupby("Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    return category_profit