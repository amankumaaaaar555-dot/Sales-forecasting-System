"""
eda_panel.py

EDA panel component for the
Sales Forecasting System.

Responsibilities
----------------
- Display all EDA visualizations

Author: Aman Kumar
"""

import streamlit as st


# ==========================================================
# EDA Panel
# ==========================================================

def show_eda_panel(eda_results):
    """
    Display all EDA charts.

    Parameters
    ----------
    eda_results : dict
        Output from run_eda()
    """

    st.header("📈 Exploratory Data Analysis")

    st.markdown(
        """
        Analyze trends, relationships, and feature distributions
        before training the forecasting model.
        """
    )

    st.divider()

    # ======================================================
    # Sales Trend
    # ======================================================

    st.subheader("📈 Sales Trend")

    st.plotly_chart(
        eda_results["sales_trend"],
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # Entity Performance
    # ======================================================

    st.subheader("🏪 Entity Performance")

    st.plotly_chart(
        eda_results["entity_performance"],
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # Correlation Matrix
    # ======================================================

    st.subheader("🔗 Correlation Matrix")

    st.plotly_chart(
        eda_results["correlation_matrix"],
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # Feature Distributions
    # ======================================================

    st.subheader("📊 Feature Distributions")

    for feature_name, figure in eda_results["feature_distributions"].items():

        with st.expander(f"Distribution of {feature_name}", expanded=False):

            st.plotly_chart(
                figure,
                use_container_width=True
            )