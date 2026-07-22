"""
model_comparison.py

Train and compare multiple machine learning models.

Responsibilities
----------------
- Train all available models
- Compare model performance
- Measure training and prediction time
- Return comparison dataframe

Author: Aman Kumar
"""

import time
import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from comparison.model_factory import (
    get_model,
    get_available_models
)

from trainer import train_selected_model


# ==========================================================
# Compare Models
# ==========================================================

def compare_models(
    X_train,
    X_test,
    y_train,
    y_test
):
    """
    Train all available models and compare their performance.

    Parameters
    ----------
    X_train : pd.DataFrame
    X_test : pd.DataFrame
    y_train : pd.Series
    y_test : pd.Series

    Returns
    -------
    pd.DataFrame
        Comparison table of all models.
    """

    results = []

    # ------------------------------------------------------
    # Train every available model
    # ------------------------------------------------------

    for model_name in get_available_models():

        model = get_model(model_name)

        # --------------------------------------------------
        # Measure Training Time
        # --------------------------------------------------

        train_start = time.perf_counter()

        model = train_selected_model(
            model,
            X_train,
            y_train
        )

        train_end = time.perf_counter()

        training_time = round(
            train_end - train_start,
            4
        )

        # --------------------------------------------------
        # Measure Prediction Time
        # --------------------------------------------------

        prediction_start = time.perf_counter()

        predictions = model.predict(
            X_test
        )

        prediction_end = time.perf_counter()

        prediction_time = round(
            prediction_end - prediction_start,
            4
        )

        # --------------------------------------------------
        # Evaluation Metrics
        # --------------------------------------------------

        mae = mean_absolute_error(
            y_test,
            predictions
        )

        mse = mean_squared_error(
            y_test,
            predictions
        )

        rmse = mse ** 0.5

        r2 = r2_score(
            y_test,
            predictions
        )

        # --------------------------------------------------
        # Store Results
        # --------------------------------------------------

        results.append({

            "Model": model_name,

            "Training Time (s)": training_time,

            "Prediction Time (s)": prediction_time,

            "Features": X_train.shape[1],

            "MAE": round(mae, 2),

            "RMSE": round(rmse, 2),

            "R2 Score": round(r2, 4)

        })

    # ------------------------------------------------------
    # Create Comparison DataFrame
    # ------------------------------------------------------

    comparison_df = pd.DataFrame(results)

    comparison_df.sort_values(

        by="R2 Score",

        ascending=False,

        inplace=True

    )

    comparison_df.reset_index(

        drop=True,

        inplace=True

    )

    return comparison_df