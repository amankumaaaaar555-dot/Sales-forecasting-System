"""
evaluator.py

Model evaluation module for the
Sales Forecasting System.

Responsibilities
----------------
- Calculate regression metrics
- Generate evaluation report
- Return evaluation results

Author: Aman Kumar
"""

import logging
import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger(__name__)


# ==========================================================
# MAE
# ==========================================================

def calculate_mae(y_true, predictions):
    """
    Calculate Mean Absolute Error.
    """

    return mean_absolute_error(
        y_true,
        predictions
    )


# ==========================================================
# MSE
# ==========================================================

def calculate_mse(y_true, predictions):
    """
    Calculate Mean Squared Error.
    """

    return mean_squared_error(
        y_true,
        predictions
    )


# ==========================================================
# RMSE
# ==========================================================

def calculate_rmse(y_true, predictions):
    """
    Calculate Root Mean Squared Error.
    """

    mse = calculate_mse(
        y_true,
        predictions
    )

    return np.sqrt(mse)


# ==========================================================
# R² Score
# ==========================================================

def calculate_r2(y_true, predictions):
    """
    Calculate R² Score.
    """

    return r2_score(
        y_true,
        predictions
    )


# ==========================================================
# Public Evaluation Function
# ==========================================================

def evaluate_model(training_results):
    """
    Evaluate trained model.
    """

    logger.info("=" * 60)
    logger.info("Evaluating trained model...")
    logger.info("=" * 60)

    y_test = training_results["y_test"]

    predictions = training_results["predictions"]

    evaluation_results = {

        "MAE": calculate_mae(
            y_test,
            predictions
        ),

        "MSE": calculate_mse(
            y_test,
            predictions
        ),

        "RMSE": calculate_rmse(
            y_test,
            predictions
        ),

        "R2 Score": calculate_r2(
            y_test,
            predictions
        )
    }

    logger.info("Model evaluation completed.")

    return evaluation_results