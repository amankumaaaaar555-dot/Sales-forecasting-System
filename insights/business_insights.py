"""
business_insights.py

Generate business insights for the Enterprise Sales Dataset.

Author: Aman Kumar
"""

import pandas as pd


def generate_business_insights(df: pd.DataFrame):
    """
    Generate business insights from enterprise sales data.
    """

    insights = {}

    # ======================================================
    # Total Sales
    # ======================================================

    insights["total_sales"] = round(
        df["Total_Amount"].sum(),
        2
    )

    # ======================================================
    # Average Sales
    # ======================================================

    insights["average_sales"] = round(
        df["Total_Amount"].mean(),
        2
    )

    # ======================================================
    # Maximum Sale
    # ======================================================

    insights["maximum_sales"] = round(
        df["Total_Amount"].max(),
        2
    )

    # ======================================================
    # Minimum Sale
    # ======================================================

    insights["minimum_sales"] = round(
        df["Total_Amount"].min(),
        2
    )

    # ======================================================
    # Highest Sales Region
    # ======================================================

    region_sales = (
        df.groupby("Region_Name")["Total_Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    insights["highest_region"] = region_sales.index[0]
    insights["highest_region_sales"] = round(region_sales.iloc[0], 2)

    insights["lowest_region"] = region_sales.index[-1]
    insights["lowest_region_sales"] = round(region_sales.iloc[-1], 2)

    # ======================================================
    # Best Selling Product
    # ======================================================

    product_sales = (
        df.groupby("Product_Name")["Quantity"]
        .sum()
        .sort_values(ascending=False)
    )

    insights["best_product"] = product_sales.index[0]
    insights["best_product_quantity"] = int(product_sales.iloc[0])

    # ======================================================
    # Most Used Payment Method
    # ======================================================

    insights["top_payment_method"] = (
        df["Payment_Method"]
        .mode()
        .iloc[0]
    )

    return insights