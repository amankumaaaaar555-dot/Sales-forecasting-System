"""
metrics_panel.py

Enterprise Dashboard Metrics

Author: Aman Kumar
"""

import streamlit as st


def show_metrics_panel(
    df,
    model_name=None,
    evaluation_results=None,
    forecast_df=None
):

    st.header("📊 Enterprise Dashboard Overview")

    total_records = len(df)

    total_sales = df["Total_Amount"].sum()

    average_sale = df["Total_Amount"].mean()

    total_customers = df["Customer_ID"].nunique()

    total_regions = df["Region_Name"].nunique()

    forecast_periods = (
        len(forecast_df)
        if forecast_df is not None
        else 0
    )

    r2 = None

    if evaluation_results:

        r2 = evaluation_results.get("R2 Score")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📄 Total Transactions",
            f"{total_records:,}"
        )

        st.metric(
            "👥 Customers",
            total_customers
        )

    with col2:

        st.metric(
            "💰 Total Revenue",
            f"₹ {total_sales:,.2f}"
        )

        st.metric(
            "📈 Average Transaction",
            f"₹ {average_sale:,.2f}"
        )

    with col3:

        st.metric(
            "🌍 Regions",
            total_regions
        )

        if model_name:

            st.metric(
                "🤖 Selected Model",
                model_name
            )

        if r2 is not None:

            st.metric(
                "🎯 R² Score",
                f"{r2:.4f}"
            )

        if forecast_df is not None:

            st.metric(
                "🔮 Forecast Days",
                forecast_periods
            )

    st.divider()