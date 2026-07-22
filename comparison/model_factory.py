"""
model_factory.py

Factory for creating machine learning models.

Responsibilities
----------------
- Create machine learning models
- Return available model names
- Centralize model configuration

Author: Aman Kumar
"""

from sklearn.linear_model import LinearRegression

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    ExtraTreesRegressor
)

from config import RANDOM_STATE


# ==========================================================
# Model Factory
# ==========================================================

def get_model(model_name: str):
    """
    Return a fresh machine learning model instance.

    Parameters
    ----------
    model_name : str
        Name of the machine learning model.

    Returns
    -------
    sklearn.base.RegressorMixin
    """

    models = {

        "Linear Regression": LinearRegression(),

        "Random Forest": RandomForestRegressor(
            n_estimators=100,
            random_state=RANDOM_STATE
        ),

        "Gradient Boosting": GradientBoostingRegressor(
            random_state=RANDOM_STATE
        ),

        "Extra Trees": ExtraTreesRegressor(
            n_estimators=100,
            random_state=RANDOM_STATE
        )

    }

    if model_name not in models:

        raise ValueError(
            f"Unsupported model: {model_name}"
        )

    return models[model_name]


# ==========================================================
# Available Models
# ==========================================================

def get_available_models():
    """
    Return the list of supported machine learning models.
    """

    return sorted(

        [

            "Linear Regression",

            "Random Forest",

            "Gradient Boosting",

            "Extra Trees"

        ]

    )