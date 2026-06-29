"""
training_pipeline.py

Training pipeline for the
Sales Forecasting System.

Responsibilities
----------------
- Validate dataset
- Preprocess dataset
- Display dataset
- Perform EDA
- Feature engineering
- Train model
- Evaluate model

Author: Aman Kumar
"""

import streamlit as st

from validator import validate_dataset
from preprocessing import preprocess_data
from eda import run_eda
from feature_engineering import engineer_features
from trainer import train_model
from evaluator import evaluate_model

from components.validation_panel import show_validation_panel
from components.dataset_panel import show_dataset_panel
from components.eda_panel import show_eda_panel
from components.evaluation_panel import show_evaluation_panel

from dashboard.metrics_panel import show_metrics_panel
from dashboard.charts_panel import show_charts_panel


# ==========================================================
# Training Pipeline
# ==========================================================

def run_training_pipeline(
    df,
    selected_model,
    train_size,
    random_state,
    split_method
):
    """
    Execute the complete training pipeline.
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
    # Dataset Preview
    # ------------------------------------------------------

    show_dataset_panel(processed_df)

    # ------------------------------------------------------
    # Exploratory Data Analysis
    # ------------------------------------------------------

    eda_results = run_eda(processed_df)

    show_eda_panel(eda_results)

    # ------------------------------------------------------
    # Feature Engineering
    # ------------------------------------------------------

    feature_df = engineer_features(processed_df)

    st.success("✅ Feature engineering completed successfully.")

    # ------------------------------------------------------
    # Model Training
    # ------------------------------------------------------

    training_results = train_model(
        feature_df,
        model_name=selected_model,
        train_size=train_size / 100,
        random_state=random_state,
        split_method=split_method
    )

    st.success("✅ Model training completed successfully.")

    # ------------------------------------------------------
    # Model Evaluation
    # ------------------------------------------------------

    evaluation_results = evaluate_model(
        training_results
    )

    # ------------------------------------------------------
    # Dashboard Metrics
    # ------------------------------------------------------

    show_metrics_panel(
        df=processed_df,
        model_name=selected_model,
        evaluation_results=evaluation_results
    )

    # ------------------------------------------------------
    # Dashboard Charts
    # ------------------------------------------------------

    show_charts_panel(
        processed_df
    )

    # ------------------------------------------------------
    # Evaluation Panel
    # ------------------------------------------------------

    show_evaluation_panel(
        evaluation_results
    )

    st.success("✅ Model evaluation completed successfully.")