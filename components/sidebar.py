"""
sidebar.py

Sidebar component for the
Sales Forecasting System.

Author: Aman Kumar
"""

import streamlit as st

from config import DEFAULT_FORECAST_HORIZON


# ==========================================================
# Sidebar Component
# ==========================================================

def show_sidebar():
    """
    Display sidebar controls.

    Returns
    -------
    tuple
    """

    # ======================================================
    # Branding
    # ======================================================

    st.sidebar.title("📈 Sales Forecasting")

    st.sidebar.caption(
        "Enterprise Analytics Platform"
    )

    st.sidebar.markdown("---")

    # ======================================================
    # Settings
    # ======================================================

    st.sidebar.header("⚙️ Settings")

    st.sidebar.markdown("---")

    # ======================================================
    # Application Mode
    # ======================================================

    st.sidebar.subheader("🚀 Application Mode")

    application_mode = st.sidebar.radio(
        "Select Mode",
        [
            "Training",
            "Forecasting"
        ]
    )

    st.sidebar.markdown("---")

    # ======================================================
    # Dataset
    # ======================================================

    st.sidebar.subheader("📂 Dataset")

    dataset_option = st.sidebar.radio(
        "Dataset Source",
        [
            "Use Default Dataset",
            "Upload CSV File"
        ]
    )

    uploaded_file = None

    if dataset_option == "Upload CSV File":

        uploaded_file = st.sidebar.file_uploader(
            "Choose CSV File",
            type=["csv"]
        )

    st.sidebar.markdown("---")

    # ======================================================
    # Model Settings
    # ======================================================

    st.sidebar.subheader("🤖 Model Settings")

    # ---------------------------------------------
    # Training Mode
    # ---------------------------------------------

    if application_mode == "Training":

        model_list = [

            "🤖 Auto Select",

            "Linear Regression",

            "Random Forest",

            "Gradient Boosting",

            "Extra Trees"

        ]

    # ---------------------------------------------
    # Forecasting Mode
    # ---------------------------------------------

    else:

        model_list = [

            "Linear Regression",

            "Random Forest",

            "Gradient Boosting",

            "Extra Trees"

        ]

    selected_model = st.sidebar.selectbox(
        "Model",
        model_list
    )

    # ======================================================
    # Forecast Settings
    # ======================================================

    forecast_horizon = st.sidebar.slider(
        "Forecast Horizon",
        min_value=7,
        max_value=365,
        value=DEFAULT_FORECAST_HORIZON,
        step=1
    )

    # ======================================================
    # Training Settings
    # ======================================================

    train_size = st.sidebar.slider(
        "Training Data (%)",
        min_value=60,
        max_value=90,
        value=80,
        step=5
    )

    random_state = st.sidebar.number_input(
        "Random State",
        min_value=0,
        value=42
    )

    split_method = st.sidebar.selectbox(
        "Split Method",
        [
            "Time Series",
            "Random"
        ]
    )

    st.sidebar.markdown("---")

    # ======================================================
    # Pipeline Status
    # ======================================================

    st.sidebar.subheader("📌 Pipeline Status")

    st.sidebar.success("✔ Load Dataset")
    st.sidebar.success("✔ Validate Dataset")
    st.sidebar.success("✔ Preprocess Dataset")
    st.sidebar.success("✔ Exploratory Data Analysis")
    st.sidebar.success("✔ Feature Engineering")
    st.sidebar.success("✔ Train Model")
    st.sidebar.success("✔ Evaluate Model")
    st.sidebar.info("⏳ Forecast Sales")

    st.sidebar.markdown("---")

    st.sidebar.caption("Version 1.0")

    st.sidebar.caption("Developed by Aman Kumar")

    return (
        application_mode,
        dataset_option,
        uploaded_file,
        selected_model,
        forecast_horizon,
        train_size,
        random_state,
        split_method
    )