"""
validator.py

Validates datasets before they enter the ML pipeline.
"""

from dataclasses import dataclass, field
from typing import List

import pandas as pd

from config import (
    DATE_COLUMN,
    TARGET_COLUMN,
    DATE_FORMAT
)


# ==========================================================
# Validation Report
# ==========================================================

@dataclass
class ValidationReport:
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    @property
    def is_valid(self):
        return len(self.errors) == 0

    def add_error(self, message: str):
        self.errors.append(message)

    def add_warning(self, message: str):
        self.warnings.append(message)


# ==========================================================
# Individual Validation Checks
# ==========================================================

def check_empty(df, report):

    if df.empty:
        report.add_error("Dataset is empty.")


def check_required_columns(df, report):

    required_columns = [
        DATE_COLUMN,
        TARGET_COLUMN
    ]

    missing = [
        col
        for col in required_columns
        if col not in df.columns
    ]

    if missing:
        report.add_error(
            f"Missing required columns: {', '.join(missing)}"
        )


def check_duplicate_rows(df, report):

    duplicates = int(df.duplicated().sum())

    if duplicates > 0:

        report.add_warning(
            f"{duplicates} duplicate rows found."
        )


def check_missing_values(df, report):

    missing = df.isnull().sum()

    missing = missing[missing > 0]

    for column, count in missing.items():

        report.add_warning(
            f"{column}: {count} missing values."
        )


def check_date_column(df, report):

    if DATE_COLUMN not in df.columns:
        return

    try:

        pd.to_datetime(
            df[DATE_COLUMN],
            format=DATE_FORMAT
        )

    except Exception:

        report.add_error(
            f"'{DATE_COLUMN}' is not a valid datetime column."
        )


def check_target_column(df, report):

    if TARGET_COLUMN not in df.columns:
        return

    if not pd.api.types.is_numeric_dtype(df[TARGET_COLUMN]):

        report.add_error(
            f"'{TARGET_COLUMN}' must be numeric."
        )


# ==========================================================
# Main Validator
# ==========================================================

def validate_dataset(df):

    report = ValidationReport()

    check_empty(df, report)

    check_required_columns(df, report)

    check_date_column(df, report)

    check_target_column(df, report)

    check_missing_values(df, report)

    check_duplicate_rows(df, report)

    return report