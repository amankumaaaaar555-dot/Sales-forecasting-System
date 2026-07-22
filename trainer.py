"""
trainer.py

Model training module for the
Sales Forecasting System.

Responsibilities
----------------
- Prepare training data
- Split dataset
- Train selected model
- Save trained model
- Return training artifacts

Author: Aman Kumar
"""

import logging
from datetime import datetime

import joblib
import pandas as pd

from sklearn.model_selection import train_test_split

from comparison.model_factory import get_model

from config import (
    TARGET_COLUMN,
    DATE_COLUMN,
    MODEL_FOLDER
)

# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger(__name__)

# ==========================================================
# Model Directory
# ==========================================================

MODEL_DIRECTORY = MODEL_FOLDER
MODEL_DIRECTORY.mkdir(exist_ok=True)


# ==========================================================
# Prepare Training Data
# ==========================================================

def prepare_training_data(df: pd.DataFrame):
    """
    Prepare feature matrix (X) and target vector (y).
    """

    logger.info("Preparing training data...")

    X = df.drop(
        columns=[
            TARGET_COLUMN,
            DATE_COLUMN
        ],
        errors="ignore"
    )

    y = df[TARGET_COLUMN]

    return X, y


# ==========================================================
# Train/Test Split
# ==========================================================

def split_training_data(
    df,
    train_size=0.80,
    random_state=42,
    split_method="Time Series"
):
    """
    Split dataset using either
    Time Series or Random strategy.
    """

    logger.info(f"Using Split Method: {split_method}")

    # ------------------------------------------------------
    # Time Series Split
    # ------------------------------------------------------

    if split_method == "Time Series":

        df = df.sort_values(DATE_COLUMN)

        split_index = int(len(df) * train_size)

        train_df = df.iloc[:split_index]
        test_df = df.iloc[split_index:]

        X_train = train_df.drop(
            columns=[
                TARGET_COLUMN,
                DATE_COLUMN
            ],
            errors="ignore"
        )

        y_train = train_df[TARGET_COLUMN]

        X_test = test_df.drop(
            columns=[
                TARGET_COLUMN,
                DATE_COLUMN
            ],
            errors="ignore"
        )

        y_test = test_df[TARGET_COLUMN]

        return X_train, X_test, y_train, y_test

    # ------------------------------------------------------
    # Random Split
    # ------------------------------------------------------

    X, y = prepare_training_data(df)

    return train_test_split(
        X,
        y,
        train_size=train_size,
        random_state=random_state
    )


# ==========================================================
# Train Selected Model
# ==========================================================

def train_selected_model(
    model,
    X_train,
    y_train
):
    """
    Train selected model.
    """

    logger.info("Training model...")

    model.fit(
        X_train,
        y_train
    )

    return model


# ==========================================================
# Save Model
# ==========================================================

def save_model(
    model,
    model_name,
    feature_columns
):
    """
    Save trained model together with metadata.
    """

    filename = (
        model_name
        .lower()
        .replace(" ", "_")
        + ".pkl"
    )

    model_path = MODEL_DIRECTORY / filename

    model_package = {

        "model": model,

        "model_name": model_name,

        "feature_columns": feature_columns,

        "trained_on": datetime.now().isoformat()

    }

    joblib.dump(
        model_package,
        model_path
    )

    logger.info(f"Model saved to {model_path}")

    return model_path


# ==========================================================
# Public Training Pipeline
# ==========================================================

def train_model(
    df,
    model_name="Linear Regression",
    train_size=0.80,
    random_state=42,
    split_method="Time Series"
):
    """
    Complete model training pipeline.
    """

    logger.info("=" * 60)
    logger.info("Starting Model Training...")
    logger.info("=" * 60)

    # ------------------------------------------------------
    # Split Dataset
    # ------------------------------------------------------

    X_train, X_test, y_train, y_test = split_training_data(
        df,
        train_size=train_size,
        random_state=random_state,
        split_method=split_method
    )

    # ------------------------------------------------------
    # Load Selected Model
    # ------------------------------------------------------

    model = get_model(model_name)

    # ------------------------------------------------------
    # Train Model
    # ------------------------------------------------------

    model = train_selected_model(
        model,
        X_train,
        y_train
    )

    # ------------------------------------------------------
    # Predictions
    # ------------------------------------------------------

    predictions = model.predict(
        X_test
    )

    feature_columns = list(X_train.columns)

    # ------------------------------------------------------
    # Save Model
    # ------------------------------------------------------

    model_path = save_model(
        model,
        model_name,
        feature_columns
    )

    logger.info("Model training completed successfully.")

    return {

        "model": model,

        "model_name": model_name,

        "model_path": str(model_path),

        "feature_columns": feature_columns,

        "X_train": X_train,
        "X_test": X_test,

        "y_train": y_train,
        "y_test": y_test,

        "predictions": predictions

    }