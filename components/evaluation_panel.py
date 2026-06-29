"""
evaluation_panel.py

Evaluation panel component for the
Sales Forecasting System.

Responsibilities
----------------
- Display model evaluation metrics

Author: Aman Kumar
"""

import streamlit as st


# ==========================================================
# Evaluation Panel
# ==========================================================

def show_evaluation_panel(evaluation_results):
    """
    Display evaluation metrics.

    Parameters
    ----------
    evaluation_results : dict
    """

    st.header("📊 Model Evaluation")

    st.markdown(
        """
        These metrics indicate how well the trained model
        predicts sales on the test dataset.
        """
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "MAE",
            f"{evaluation_results['MAE']:.2f}"
        )

        st.metric(
            "RMSE",
            f"{evaluation_results['RMSE']:.2f}"
        )

    with col2:

        st.metric(
            "MSE",
            f"{evaluation_results['MSE']:.2f}"
        )

        st.metric(
            "R² Score",
            f"{evaluation_results['R2 Score']:.4f}"
        )

    st.divider()