"""
feature_engineering.py

Feature engineering module for the
Sales Forecasting System.

Responsibilities
----------------
- Create date-based features
- Select model features
- Return engineered dataset

Author: Aman Kumar
"""

import logging
import pandas as pd

from config import DATE_COLUMN

logger = logging.getLogger(__name__)


# ==========================================================
# Create Date Features
# ==========================================================

def create_date_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extract useful features from the date column.
    """

    logger.info("Creating date features...")

    df["Year"] = df[DATE_COLUMN].dt.year
    df["Month"] = df[DATE_COLUMN].dt.month
    df["Quarter"] = df[DATE_COLUMN].dt.quarter
    df["Week"] = df[DATE_COLUMN].dt.isocalendar().week.astype(int)
    df["Day"] = df[DATE_COLUMN].dt.day
    df["DayOfWeek"] = df[DATE_COLUMN].dt.dayofweek

    return df


# ==========================================================
# Select Features
# ==========================================================

def select_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Placeholder for future feature selection.
    Currently returns the dataframe unchanged.
    """

    logger.info("Selecting features...")

    return df


# ==========================================================
# Public Pipeline
# ==========================================================

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Complete feature engineering pipeline.
    """

    logger.info("=" * 60)
    logger.info("Starting Feature Engineering...")
    logger.info("=" * 60)

    feature_df = df.copy()

    feature_df = create_date_features(feature_df)

    feature_df = select_features(feature_df)

    logger.info("Feature engineering completed successfully.")

    return feature_df