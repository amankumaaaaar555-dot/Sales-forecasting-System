"""
model_factory.py

Factory for creating machine learning models.

Author: Aman Kumar
"""

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    ExtraTreesRegressor
)


# ==========================================================
# Available Models
# ==========================================================

AVAILABLE_MODELS = {

    "Linear Regression": LinearRegression(),

    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),

    "Gradient Boosting": GradientBoostingRegressor(
        random_state=42
    ),

    "Extra Trees": ExtraTreesRegressor(
        n_estimators=100,
        random_state=42
    )

}


# ==========================================================
# Model Factory
# ==========================================================

def get_model(model_name):
    """
    Return a machine learning model.

    Parameters
    ----------
    model_name : str

    Returns
    -------
    sklearn model
    """

    if model_name not in AVAILABLE_MODELS:

        raise ValueError(
            f"Unsupported model: {model_name}"
        )

    return AVAILABLE_MODELS[model_name]


# ==========================================================
# Available Model Names
# ==========================================================

def get_available_models():
    """
    Return list of available models.
    """

    return list(
        AVAILABLE_MODELS.keys()
    )