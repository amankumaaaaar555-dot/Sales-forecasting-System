"""
model_selector.py

Select the best machine learning model
based on evaluation metrics.

Author: Aman Kumar
"""

import pandas as pd


# ==========================================================
# Best Model Selector
# ==========================================================

def select_best_model(comparison_df: pd.DataFrame):
    """
    Select the best model from the comparison table.

    Parameters
    ----------
    comparison_df : pd.DataFrame

    Returns
    -------
    dict
    """

    if comparison_df.empty:

        raise ValueError(
            "Comparison dataframe is empty."
        )

    best = comparison_df.iloc[0]

    return {

        "model_name": best["Model"],

        "mae": best["MAE"],

        "rmse": best["RMSE"],

        "r2_score": best["R2 Score"]

    }


# ==========================================================
# Ranking
# ==========================================================

def get_model_ranking(comparison_df: pd.DataFrame):
    """
    Return the complete ranking table.
    """

    ranking = comparison_df.copy()

    ranking.insert(
        0,
        "Rank",
        range(
            1,
            len(ranking) + 1
        )
    )

    return ranking