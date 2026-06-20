def get_recommendations(df):

    recommendations = []

    # Core Metrics

    total_sales = df["Sales"].sum()

    total_profit = df["Profit"].sum()

    profit_margin = (
        total_profit / total_sales
    ) * 100

    avg_discount = (
        df["Discount"].mean()
    ) * 100

    total_customers = (
        df["Customer ID"].nunique()
    )

    # Rule 1

    if profit_margin < 10:

        recommendations.append(
            "Profit margin is critically low. Review pricing and operational costs."
        )

    elif profit_margin < 15:

        recommendations.append(
            "Profit margin is below ideal levels. Consider improving pricing strategy."
        )

    # Rule 2

    if avg_discount > 20:

        recommendations.append(
            "High discount levels detected. Excessive discounts may be reducing profitability."
        )

    # Rule 3

    if total_customers < 500:

        recommendations.append(
            "Customer base is relatively small. Focus on customer acquisition."
        )

    # Rule 4

    if total_profit < 0:

        recommendations.append(
            "Business is currently operating at a loss. Immediate intervention is required."
        )

    # Default

    if len(recommendations) == 0:

        recommendations.append(
            "Business performance appears healthy."
        )

    return recommendations