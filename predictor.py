"""
predictor.py

Future Sales Forecasting Module

Responsibilities
----------------
- Load trained model
- Generate future dates
- Create future dataset
- Engineer future features
- Align feature columns
- Predict future sales

Author: Aman Kumar
"""

import logging
from pathlib import Path

import joblib
import pandas as pd

from config import (
    DATE_COLUMN,
    FORECAST_FREQUENCY
)

from feature_engineering import engineer_features

# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger(__name__)

# ==========================================================
# Model Directory
# ==========================================================

MODEL_DIRECTORY = Path("saved_models")


# ==========================================================
# Get Model Path
# ==========================================================

def get_model_path(model_name: str) -> Path:
    """
    Return the saved model path.
    """

    filename = (
        model_name
        .lower()
        .replace(" ", "_")
        + ".pkl"
    )

    return MODEL_DIRECTORY / filename


# ==========================================================
# Load Saved Model
# ==========================================================

def load_saved_model(model_name: str):
    """
    Load trained model package.
    """

    model_path = get_model_path(model_name)

    if not model_path.exists():

        raise FileNotFoundError(
            f"Model '{model_name}' has not been trained yet."
        )

    logger.info(f"Loading model from {model_path}")

    return joblib.load(model_path)


# ==========================================================
# Generate Future Dates
# ==========================================================

def generate_future_dates(
    last_date,
    forecast_horizon
):
    """
    Generate future dates.
    """

    future_dates = pd.date_range(
        start=last_date,
        periods=forecast_horizon + 1,
        freq=FORECAST_FREQUENCY
    )[1:]

    return future_dates


# ==========================================================
# Create Future Dataset
# ==========================================================

def create_future_dataset(
    processed_df,
    future_dates
):
    """
    Create future dataset using
    the last available row.
    """

    logger.info("Creating future dataset...")

    last_row = processed_df.iloc[-1].copy()

    future_rows = []

    for future_date in future_dates:

        row = last_row.copy()

        row[DATE_COLUMN] = future_date

        future_rows.append(row)

    future_df = pd.DataFrame(future_rows)

    return future_df


# ==========================================================
# Engineer Future Dataset
# ==========================================================

def engineer_future_dataset(
    future_df
):
    """
    Apply feature engineering.
    """

    logger.info("Engineering future dataset...")

    return engineer_features(
        future_df
    )


# ==========================================================
# Align Feature Columns
# ==========================================================

def align_feature_columns(
    future_df,
    feature_columns
):
    """
    Keep only columns used during training.
    """

    return future_df[
        feature_columns
    ]


# ==========================================================
# Predict Future Sales
# ==========================================================

def predict_future_sales(
    model,
    feature_df
):
    """
    Predict future sales.
    """

    logger.info("Predicting future sales...")

    predictions = model.predict(
        feature_df
    )

    return predictions


# ==========================================================
# Forecast Pipeline
# ==========================================================

def forecast_sales(
    processed_df,
    model_name,
    forecast_horizon
):
    """
    Complete forecasting pipeline.
    """

    logger.info("=" * 60)
    logger.info("Starting Forecast...")
    logger.info("=" * 60)

    # ------------------------------------------------------
    # Load Model
    # ------------------------------------------------------

    saved_package = load_saved_model(
        model_name
    )

    model = saved_package["model"]

    feature_columns = saved_package[
        "feature_columns"
    ]

    # ------------------------------------------------------
    # Future Dates
    # ------------------------------------------------------

    last_date = processed_df[
        DATE_COLUMN
    ].max()

    future_dates = generate_future_dates(
        last_date,
        forecast_horizon
    )

    # ------------------------------------------------------
    # Future Dataset
    # ------------------------------------------------------

    future_df = create_future_dataset(
        processed_df,
        future_dates
    )

    # ------------------------------------------------------
    # Feature Engineering
    # ------------------------------------------------------

    future_df = engineer_future_dataset(
        future_df
    )

    # ------------------------------------------------------
    # Align Columns
    # ------------------------------------------------------

    feature_df = align_feature_columns(
        future_df,
        feature_columns
    )

    # ------------------------------------------------------
    # Predict
    # ------------------------------------------------------

    predictions = predict_future_sales(
        model,
        feature_df
    )

    # ------------------------------------------------------
    # Final Forecast
    # ------------------------------------------------------

    forecast_df = pd.DataFrame({

        DATE_COLUMN: future_dates,

        "Predicted_Sales": predictions

    })

    logger.info("Forecast completed successfully.")

    return forecast_df