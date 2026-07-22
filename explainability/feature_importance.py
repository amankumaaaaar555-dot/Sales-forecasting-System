"""
feature_importance.py

Explainable AI module.

Author: Aman Kumar
"""

import pandas as pd


# ==========================================================
# Feature Importance
# ==========================================================

def get_feature_importance(
    model,
    feature_columns
):
    """
    Extract feature importance from tree-based models.

    Parameters
    ----------
    model : trained model

    feature_columns : list

    Returns
    -------
    pd.DataFrame | None
    """

    if not hasattr(model, "feature_importances_"):

        return None

    importance_df = pd.DataFrame({

        "Feature": feature_columns,

        "Importance": model.feature_importances_

    })

    importance_df.sort_values(

        by="Importance",

        ascending=False,

        inplace=True

    )

    importance_df.reset_index(

        drop=True,

        inplace=True

    )

    return importance_df