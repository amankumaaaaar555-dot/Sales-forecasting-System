"""
training_service.py

Business logic for model training.

Responsibilities
----------------
- Handle manual training
- Handle AutoML training
- Return unified results

Author: Aman Kumar
"""

import logging

from trainer import train_model
from evaluator import evaluate_model

from comparison.auto_ml import run_automl


# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger(__name__)


# ==========================================================
# Training Service
# ==========================================================

def execute_training(
    df,
    selected_model,
    train_size,
    random_state,
    split_method
):
    """
    Execute either Manual Training
    or AutoML.
    """

    logger.info("=" * 60)
    logger.info("Training Service Started")
    logger.info("=" * 60)

    # ======================================================
    # AutoML
    # ======================================================

    if selected_model == "🤖 Auto Select":

        logger.info("Running AutoML...")

        training_results = train_model(
            df,
            model_name="Random Forest",
            train_size=train_size,
            random_state=random_state,
            split_method=split_method
        )

        automl_results = run_automl(
            training_results["X_train"],
            training_results["X_test"],
            training_results["y_train"],
            training_results["y_test"]
        )

        return {

            "mode": "automl",

            "training_results": training_results,

            "evaluation_results": evaluate_model(
                training_results
            ),

            "automl_results": automl_results

        }

    # ======================================================
    # Manual Training
    # ======================================================

    logger.info(f"Running {selected_model}")

    training_results = train_model(
        df,
        model_name=selected_model,
        train_size=train_size,
        random_state=random_state,
        split_method=split_method
    )

    evaluation_results = evaluate_model(
        training_results
    )

    return {

        "mode": "manual",

        "training_results": training_results,

        "evaluation_results": evaluation_results

    }