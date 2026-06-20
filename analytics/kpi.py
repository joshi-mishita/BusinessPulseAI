import pandas as pd

def calculate_kpis(df):

    total_revenue = df["Sales"].sum()

    total_profit = df["Profit"].sum()

    total_orders = len(df)

    total_customers = df["Customer ID"].nunique()

    avg_order_value = total_revenue / total_orders

    profit_margin = (total_profit / total_revenue) * 100

    return {
    "Revenue": float(round(total_revenue, 2)),
    "Profit": float(round(total_profit, 2)),
    "Orders": int(total_orders),
    "Customers": int(total_customers),
    "Average Order Value": float(round(avg_order_value, 2)),
    "Profit Margin": float(round(profit_margin, 2))
}