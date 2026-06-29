"""
config.py

Central configuration file for the
Sales Forecasting System.

Author: Aman Kumar
"""

from pathlib import Path

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

DATASET_FOLDER = BASE_DIR / "datasets"
OUTPUT_FOLDER = BASE_DIR / "outputs"
MODEL_FOLDER = BASE_DIR / "saved_models"

# ==========================================================
# Dataset
# ==========================================================

DEFAULT_DATASET_NAME = "walmart.csv"

DATE_COLUMN = "Date"

TARGET_COLUMN = "Weekly_Sales"

DATE_FORMAT = "%d-%m-%Y"

# ==========================================================
# Dataset Schema
# ==========================================================

ID_COLUMNS = [
    "Store"
]

CATEGORICAL_COLUMNS = [
    "Holiday_Flag"
]

NUMERICAL_COLUMNS = [
    "Temperature",
    "Fuel_Price",
    "CPI",
    "Unemployment"
]

# ==========================================================
# Model Configuration
# ==========================================================

RANDOM_STATE = 42

TEST_SIZE = 0.20

# ==========================================================
# Forecast Configuration
# ==========================================================

# Frequency:
# D = Daily
# W = Weekly
# M = Monthly

FORECAST_FREQUENCY = "W"

DEFAULT_FORECAST_HORIZON = 30

DEFAULT_SPLIT_METHOD = "Time Series"