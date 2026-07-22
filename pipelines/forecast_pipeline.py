"""
forecast_pipeline.py

Forecast pipeline for the
Sales Forecasting System.

Responsibilities
----------------
- Validate dataset
- Preprocess dataset
- Generate future forecasts
- Display forecast

Author: Aman Kumar
"""

import streamlit as st

from validator import validate_dataset
from preprocessing import preprocess_data
from predictor import forecast_sales

from components.validation_panel import show_validation_panel
from components.prediction_panel import show_prediction_panel

from dashboard.metrics_panel import show_metrics_panel
from dashboard.charts_panel import show_charts_panel
from components.download_panel import show_download_panel


# ==========================================================
# Forecast Pipeline
# ==========================================================

def run_forecast_pipeline(
    df,
    selected_model,
    forecast_horizon
):
    """
    Execute the complete forecasting pipeline.
    """

    # ------------------------------------------------------
    # Dataset Validation
    # ------------------------------------------------------

    report = validate_dataset(df)

    show_validation_panel(report)

    if not report.is_valid:
        return

    # ------------------------------------------------------
    # Dataset Preprocessing
    # ------------------------------------------------------

    processed_df = preprocess_data(df)

    st.success("✅ Dataset preprocessing completed successfully.")

    # ------------------------------------------------------
    # Forecast Future Sales
    # ------------------------------------------------------

    forecast_df = forecast_sales(
        processed_df=processed_df,
        model_name=selected_model,
        forecast_horizon=forecast_horizon
    )

    st.success("✅ Sales forecast generated successfully.")

    # ------------------------------------------------------
    # Dashboard Metrics
    # ------------------------------------------------------

    show_metrics_panel(
        df=processed_df,
        model_name=selected_model,
        forecast_df=forecast_df
    )

    # ------------------------------------------------------
    # Dashboard Charts
    # ------------------------------------------------------

    show_charts_panel(
        processed_df,
        forecast_df
    )

    # ------------------------------------------------------
    # Prediction Panel
    # ------------------------------------------------------

    show_prediction_panel(
        forecast_df
    )
    show_download_panel(
    forecast_df=forecast_df
)