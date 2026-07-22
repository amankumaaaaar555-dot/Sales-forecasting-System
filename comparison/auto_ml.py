"""
auto_ml.py

Automatic Machine Learning (AutoML)

Responsibilities
----------------
- Train all available models
- Compare model performance
- Select the best model
- Return AutoML results

Author: Aman Kumar
"""

import logging

from comparison.model_comparison import compare_models
from comparison.model_selector import (
    select_best_model,
    get_model_ranking
)

# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger(__name__)


# ==========================================================
# AutoML Pipeline
# ==========================================================

def run_automl(
    X_train,
    X_test,
    y_train,
    y_test
):
    """
    Execute the complete AutoML pipeline.

    Parameters
    ----------
    X_train : pd.DataFrame
    X_test : pd.DataFrame
    y_train : pd.Series
    y_test : pd.Series

    Returns
    -------
    dict
        AutoML results.
    """

    logger.info("=" * 60)
    logger.info("Starting AutoML...")
    logger.info("=" * 60)

    # ------------------------------------------------------
    # Compare All Models
    # ------------------------------------------------------

    comparison_df = compare_models(
        X_train,
        X_test,
        y_train,
        y_test
    )

    # ------------------------------------------------------
    # Select Best Model
    # ------------------------------------------------------

    best_model = select_best_model(
        comparison_df
    )

    # ------------------------------------------------------
    # Ranking
    # ------------------------------------------------------

    ranking = get_model_ranking(
        comparison_df
    )

    logger.info(
        f"Best Model: {best_model['model_name']}"
    )

    logger.info("AutoML completed successfully.")

    return {

        "comparison_df": comparison_df,

        "ranking": ranking,

        "best_model": best_model

    }


# ==========================================================
# Utility
# ==========================================================

def get_best_model_name(results: dict):
    """
    Return the best model name from AutoML results.
    """

    return results["best_model"]["model_name"]


def get_best_model_metrics(results: dict):
    """
    Return the best model metrics.
    """

    return results["best_model"]