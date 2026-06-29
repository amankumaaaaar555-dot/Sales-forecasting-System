"""
metrics_panel.py

Dashboard KPI Metrics Panel

Responsibilities
----------------
- Display key business metrics
- Reusable in Training and Forecasting modes

Author: Aman Kumar
"""

import streamlit as st

from config import (
    TARGET_COLUMN,
    ID_COLUMNS
)


# ==========================================================
# Metrics Panel
# ==========================================================

def show_metrics_panel(
    df,
    model_name=None,
    evaluation_results=None,
    forecast_df=None
):
    """
    Display dashboard KPI cards.

    Parameters
    ----------
    df : pd.DataFrame
        Original or processed dataset

    model_name : str, optional
        Selected model

    evaluation_results : dict, optional
        Output from evaluator.py

    forecast_df : pd.DataFrame, optional
        Forecast dataframe
    """

    st.header("📊 Dashboard Overview")

    # ======================================================
    # Calculate KPIs
    # ======================================================

    total_records = len(df)

    total_sales = df[TARGET_COLUMN].sum()

    average_sales = df[TARGET_COLUMN].mean()

    total_stores = (
        df[ID_COLUMNS[0]].nunique()
        if ID_COLUMNS
        else 0
    )

    forecast_periods = (
        len(forecast_df)
        if forecast_df is not None
        else 0
    )

    r2_score = None

    if evaluation_results is not None:

        r2_score = evaluation_results.get(
            "R2 Score",
            None
        )

    # ======================================================
    # KPI Cards
    # ======================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📄 Total Records",
            f"{total_records:,}"
        )

        st.metric(
            "🏪 Stores",
            total_stores
        )

    with col2:

        st.metric(
            "💰 Total Sales",
            f"{total_sales:,.2f}"
        )

        st.metric(
            "📈 Average Sales",
            f"{average_sales:,.2f}"
        )

    with col3:

        if model_name:

            st.metric(
                "🤖 Model",
                model_name
            )

        if r2_score is not None:

            st.metric(
                "🎯 R² Score",
                f"{r2_score:.4f}"
            )

        if forecast_df is not None:

            st.metric(
                "🔮 Forecast Periods",
                forecast_periods
            )

    st.divider()