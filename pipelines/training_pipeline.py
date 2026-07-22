"""
training_pipeline.py

Training pipeline for the
Sales Forecasting System.

Responsibilities
----------------
- Validate dataset
- Preprocess dataset
- Perform EDA
- Feature engineering
- Execute training service
- Display evaluation
- Display model comparison

Author: Aman Kumar
"""

import streamlit as st

from validator import validate_dataset
from preprocessing import preprocess_data
from eda import run_eda
from feature_engineering import engineer_features

from services.training_service import execute_training

from components.validation_panel import show_validation_panel
from components.dataset_panel import show_dataset_panel
from components.eda_panel import show_eda_panel
from components.evaluation_panel import show_evaluation_panel

from dashboard.metrics_panel import show_metrics_panel
from dashboard.charts_panel import show_charts_panel
from insights.business_insights import generate_business_insights
from dashboard.business_insights_panel import show_business_insights_panel
from components.download_panel import show_download_panel

from comparison.model_comparison import compare_models
from comparison.model_selector import (
    select_best_model,
    get_model_ranking
)
from comparison.comparison_report import (
    show_comparison_report
)
from explainability.feature_importance import (
    get_feature_importance
)

from dashboard.feature_importance_panel import (
    show_feature_importance_panel
)


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

    # ======================================================
    # Dataset Validation
    # ======================================================

    report = validate_dataset(df)

    show_validation_panel(report)

    if not report.is_valid:
        return

    # ======================================================
    # Dataset Preprocessing
    # ======================================================

    processed_df = preprocess_data(df)

    st.success("✅ Dataset preprocessing completed successfully.")

    # ======================================================
    # Dataset Preview
    # ======================================================

    show_dataset_panel(processed_df)

    # ======================================================
    # Exploratory Data Analysis
    # ======================================================

    eda_results = run_eda(processed_df)

    show_eda_panel(eda_results)

    # ======================================================
    # Feature Engineering
    # ======================================================

    feature_df = engineer_features(processed_df)

    st.success("✅ Feature engineering completed successfully.")

    # ======================================================
    # Training Service
    # ======================================================

    service_results = execute_training(
        df=feature_df,
        selected_model=selected_model,
        train_size=train_size / 100,
        random_state=random_state,
        split_method=split_method
    )

    training_results = service_results["training_results"]
    evaluation_results = service_results["evaluation_results"]

    st.success("✅ Model training completed successfully.")

    # ======================================================
    # Dashboard Metrics
    # ======================================================

    show_metrics_panel(
        df=processed_df,
        model_name=selected_model,
        evaluation_results=evaluation_results
    )

    # ======================================================
    # Dashboard Charts
    # ======================================================

    show_charts_panel(
        processed_df
    )
    # ======================================================
# Business Insights
# ======================================================

    insights = generate_business_insights(
        processed_df
    )

    show_business_insights_panel(
        insights
    )

    # ======================================================
    # Evaluation Panel
    # ======================================================

    show_evaluation_panel(
        evaluation_results
    )
    # ======================================================
# Explainable AI
# ======================================================

    importance_df = get_feature_importance(

    training_results["model"],

    training_results["feature_columns"]

)

    show_feature_importance_panel(
    importance_df
)

    st.success("✅ Model evaluation completed successfully.")

    # ======================================================
    # Manual Training Mode
    # ======================================================

    if service_results["mode"] == "manual":

        comparison_df = compare_models(
            training_results["X_train"],
            training_results["X_test"],
            training_results["y_train"],
            training_results["y_test"]
        )

        best_model = select_best_model(
            comparison_df
        )

        ranking = get_model_ranking(
            comparison_df
        )

        show_comparison_report(
            ranking,
            best_model
        )
        show_download_panel(
    comparison_df=comparison_df,
    evaluation_results=evaluation_results,
    model_path=training_results["model_path"]
)

        st.success("✅ Model comparison completed successfully.")

    # ======================================================
    # AutoML Mode
    # ======================================================

    else:

        automl_results = service_results["automl_results"]

        show_comparison_report(
            automl_results["ranking"],
            automl_results["best_model"]
        )
        show_download_panel(
    evaluation_results=evaluation_results,
    model_path=training_results["model_path"]
)

        st.success("✅ AutoML completed successfully.")