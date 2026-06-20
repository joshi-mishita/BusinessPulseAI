import pandas as pd

def get_monthly_sales(df):

    df = df.copy()

    df["Order Date"] = pd.to_datetime(
        df["Order Date"]
    )

    monthly_sales = (
        df.groupby(
            pd.Grouper(
                key="Order Date",
                freq="ME"
            )
        )["Sales"]
        .sum()
        .reset_index()
    )

    return monthly_sales