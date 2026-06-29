"""
preprocessing.py

Data preprocessing pipeline for the Sales Forecasting System.

Responsibilities:
    - Create a copy of the dataset
    - Convert date column to datetime
    - Sort dataset chronologically
    - Remove duplicate rows
    - Reset dataframe index

Author: Aman Kumar
Project: Sales Forecasting System
"""

import logging
import pandas as pd

from config import (
    DATE_COLUMN,
    DATE_FORMAT
)

# ==========================================================
# Logger Configuration
# ==========================================================

logger = logging.getLogger(__name__)


# ==========================================================
# Helper Functions
# ==========================================================

def copy_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a copy of the dataframe.
    """

    logger.info("Creating dataframe copy...")

    return df.copy()


def convert_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert the configured date column into datetime format.
    """

    logger.info("Converting date column...")

    df[DATE_COLUMN] = pd.to_datetime(
        df[DATE_COLUMN],
        format=DATE_FORMAT
    )

    return df


def sort_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sort dataset by date.
    """

    logger.info("Sorting dataset by date...")

    return df.sort_values(by=DATE_COLUMN)


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows.
    """

    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:

        logger.info(
            f"Removing {duplicate_count} duplicate rows..."
        )

        df = df.drop_duplicates()

    return df


def reset_dataframe_index(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reset dataframe index.
    """

    logger.info("Resetting dataframe index...")

    return df.reset_index(drop=True)


# ==========================================================
# Public Preprocessing Function
# ==========================================================

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Complete preprocessing pipeline.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """

    logger.info("=" * 60)
    logger.info("Starting preprocessing pipeline...")
    logger.info("=" * 60)

    df = copy_dataframe(df)

    df = convert_date(df)

    df = sort_dataset(df)

    df = remove_duplicates(df)

    df = reset_dataframe_index(df)

    logger.info("=" * 60)
    logger.info("Preprocessing completed successfully.")
    logger.info("=" * 60)

    return df