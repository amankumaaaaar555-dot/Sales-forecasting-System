"""
Main Streamlit Application

Author: Aman Kumar
Project: Sales Forecasting System
"""

import streamlit as st

# ==========================================================
# Backend Modules
# ==========================================================

from data_loader import load_dataset

# ==========================================================
# UI Components
# ==========================================================

from components.sidebar import show_sidebar

# ==========================================================
# Pipelines
# ==========================================================

from pipelines.training_pipeline import run_training_pipeline
from pipelines.forecast_pipeline import run_forecast_pipeline

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Sales Forecasting System",
    page_icon="📈",
    layout="wide"
)
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ==========================================================
# Application Title
# ==========================================================

st.title("📈 Enterprise Sales Forecasting & Business Intelligence Platform")

st.caption(
    "AI-Powered Enterprise Sales Analytics | Machine Learning | Forecasting | Business Intelligence"
)

st.markdown("---")

st.markdown("---")

# ==========================================================
# Sidebar
# ==========================================================

(
    application_mode,
    dataset_option,
    uploaded_file,
    selected_model,
    forecast_horizon,
    train_size,
    random_state,
    split_method
) = show_sidebar()

# ==========================================================
# Dataset Loading
# ==========================================================

df = None

try:

    if dataset_option == "Use Default Dataset":

        df = load_dataset()

    elif uploaded_file is not None:

        df = load_dataset(uploaded_file)

except Exception as e:

    st.error(f"Error loading dataset: {e}")

# ==========================================================
# Run Selected Pipeline
# ==========================================================

if df is not None:

    if application_mode == "Training":

        run_training_pipeline(
            df=df,
            selected_model=selected_model,
            train_size=train_size,
            random_state=random_state,
            split_method=split_method
        )

    elif application_mode == "Forecasting":

        run_forecast_pipeline(
            df=df,
            selected_model=selected_model,
            forecast_horizon=forecast_horizon
        )

else:

    st.info("👈 Please load a dataset from the sidebar.")