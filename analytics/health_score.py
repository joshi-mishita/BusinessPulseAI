import pandas as pd

def calculate_health_score(df):

    revenue = df["Sales"].sum()

    profit = df["Profit"].sum()

    customers = df["Customer ID"].nunique()

    avg_order_value = revenue / len(df)

    avg_discount = df["Discount"].mean() * 100

    profit_margin = (profit / revenue) * 100

    # Convert metrics to scores (0-100)

    profit_score = min(max(profit_margin * 4, 0), 100)

    customer_score = min(customers / 8, 100)

    order_value_score = min(avg_order_value / 3, 100)

    revenue_score = min(revenue / 25000, 100)

    discount_score = max(100 - avg_discount * 2, 0)

    final_score = (
        0.35 * profit_score +
        0.20 * customer_score +
        0.20 * order_value_score +
        0.15 * revenue_score +
        0.10 * discount_score
    )

    return round(final_score, 2)