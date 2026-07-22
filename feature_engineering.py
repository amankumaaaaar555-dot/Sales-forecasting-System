"""
feature_engineering.py

Feature Engineering Module

Responsibilities
----------------
- Create date features
- Remove unnecessary ID columns
- Apply One-Hot Encoding
- Return ML-ready dataset

Author: Aman Kumar
"""

import logging
import pandas as pd

from config import (
    DATE_COLUMN,
    ID_COLUMNS,
    CATEGORICAL_COLUMNS
)

logger = logging.getLogger(__name__)


# ==========================================================
# Create Date Features
# ==========================================================

def create_date_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create useful date-based features.
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
# Remove ID Columns
# ==========================================================

def remove_id_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove identifier columns.
    """

    logger.info("Removing ID columns...")

    existing_columns = [
        column
        for column in ID_COLUMNS
        if column in df.columns
    ]

    df = df.drop(
        columns=existing_columns,
        errors="ignore"
    )

    return df


# ==========================================================
# One-Hot Encoding
# ==========================================================

def encode_categorical_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply One-Hot Encoding.
    """

    logger.info("Applying One-Hot Encoding...")

    existing_columns = [
        column
        for column in CATEGORICAL_COLUMNS
        if column in df.columns
    ]

    df = pd.get_dummies(
        df,
        columns=existing_columns,
        drop_first=True,
        dtype=int
    )

    return df


# ==========================================================
# Feature Selection
# ==========================================================

def select_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Placeholder for future feature selection.
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

    feature_df = remove_id_columns(feature_df)

    feature_df = encode_categorical_features(feature_df)

    feature_df = select_features(feature_df)

    logger.info("=" * 60)
    logger.info("Feature Engineering Completed Successfully")
    logger.info("=" * 60)

    return feature_df