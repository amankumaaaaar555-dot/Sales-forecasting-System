"""
comparison_report.py

Professional Model Comparison Dashboard

Author: Aman Kumar
"""

import streamlit as st
import plotly.express as px
import pandas as pd


# ==========================================================
# Comparison Report
# ==========================================================

def show_comparison_report(
    comparison_df: pd.DataFrame,
    best_model: dict
):
    """
    Display professional comparison dashboard.
    """

    st.divider()

    st.header("🏆 Model Comparison Dashboard")

    # ======================================================
    # Best Model Card
    # ======================================================

    st.success(

        f"""
### 🥇 Best Model

**{best_model["model_name"]}**

This model achieved the highest R² score.
"""
    )

    # ======================================================
    # KPI Cards
    # ======================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(

            "R² Score",

            best_model["r2_score"]

        )

    with col2:

        st.metric(

            "RMSE",

            best_model["rmse"]

        )

    with col3:

        st.metric(

            "MAE",

            best_model["mae"]

        )

    with col4:

        training_time = comparison_df.iloc[0]["Training Time (s)"]

        st.metric(

            "Training Time",

            f"{training_time} s"

        )

    st.divider()

    # ======================================================
    # Comparison Chart
    # ======================================================

    st.subheader("📈 R² Score Comparison")

    fig = px.bar(

        comparison_df,

        x="Model",

        y="R2 Score",

        text="R2 Score",

        color="R2 Score"

    )

    fig.update_layout(

        xaxis_title="Model",

        yaxis_title="R² Score"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ======================================================
    # RMSE Chart
    # ======================================================

    st.subheader("📉 RMSE Comparison")

    rmse_fig = px.bar(

        comparison_df,

        x="Model",

        y="RMSE",

        text="RMSE",

        color="RMSE"

    )

    st.plotly_chart(

        rmse_fig,

        use_container_width=True

    )

    # ======================================================
    # Ranking Table
    # ======================================================

    st.subheader("📋 Model Ranking")

    st.dataframe(

        comparison_df,

        use_container_width=True,

        hide_index=True

    )

    st.info(

        f"🏆 {best_model['model_name']} has been selected as the best performing model."

    )