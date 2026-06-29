"""
dataset_info.py

Provides summary information about datasets.

Author: Aman Kumar
Project: Sales Forecasting System
"""

import pandas as pd


# ==========================================================
# Dataset Summary
# ==========================================================

def generate_dataset_summary(df: pd.DataFrame) -> dict:
    """
    Generate a complete summary of the dataset.
    """

    return {

        "Rows": df.shape[0],

        "Columns": df.shape[1],

        "Column Names": list(df.columns),

        "Data Types": df.dtypes.astype(str).to_dict(),

        "Missing Values": df.isnull().sum().to_dict(),

        "Duplicate Rows": int(df.duplicated().sum()),

        "Memory Usage": get_memory_usage(df),

        "Numerical Columns": get_numerical_columns(df),

        "Categorical Columns": get_categorical_columns(df)

    }


# ==========================================================
# Helper Functions
# ==========================================================

def get_memory_usage(df: pd.DataFrame) -> str:
    """
    Calculate dataframe memory usage.
    """

    memory = df.memory_usage(deep=True).sum()

    return f"{memory / (1024 * 1024):.2f} MB"


def get_numerical_columns(df: pd.DataFrame) -> list:
    """
    Return all numerical columns.
    """

    return list(
        df.select_dtypes(include=["number"]).columns
    )


def get_categorical_columns(df: pd.DataFrame) -> list:
    """
    Return all categorical columns.
    """

    return list(
        df.select_dtypes(include=["object"]).columns
    )