"""
charts_panel.py

Dashboard Charts Panel

Responsibilities
----------------
- Sales Trend
- Store Performance
- Correlation Heatmap
- Forecast Chart

Author: Aman Kumar
"""

import streamlit as st
import plotly.express as px

from config import (
    DATE_COLUMN,
    TARGET_COLUMN,
    ID_COLUMNS
)


# ==========================================================
# Dashboard Charts
# ==========================================================

def show_charts_panel(
    df,
    forecast_df=None
):
    """
    Display dashboard charts.

    Parameters
    ----------
    df : pd.DataFrame

    forecast_df : pd.DataFrame, optional
    """

    st.header("📈 Dashboard Charts")

    # ======================================================
    # Sales Trend
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Sales Trend")

        trend = px.line(
            df,
            x=DATE_COLUMN,
            y=TARGET_COLUMN,
            title="Weekly Sales Trend"
        )

        st.plotly_chart(
            trend,
            use_container_width=True
        )

    # ======================================================
    # Store Performance
    # ======================================================

    with col2:

        st.subheader("Store Performance")

        store_sales = (
            df.groupby(ID_COLUMNS[0])[TARGET_COLUMN]
            .sum()
            .reset_index()
        )

        store_chart = px.bar(
            store_sales,
            x=ID_COLUMNS[0],
            y=TARGET_COLUMN,
            title="Sales by Store"
        )

        st.plotly_chart(
            store_chart,
            use_container_width=True
        )

    st.divider()

    # ======================================================
    # Forecast Chart
    # ======================================================

    if forecast_df is not None:

        st.subheader("Forecast Trend")

        fig = px.line(
            forecast_df,
            x=DATE_COLUMN,
            y="Predicted_Sales",
            markers=True,
            title="Forecasted Sales"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )