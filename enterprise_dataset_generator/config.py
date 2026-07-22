"""
config.py

Configuration settings for the
Enterprise Dataset Generator.

This file contains all configurable
parameters used while generating the
WellRx enterprise sales dataset.

Author: Aman Kumar
"""

from pathlib import Path


# ==========================================================
# Project Directories
# ==========================================================

# Current folder
BASE_DIRECTORY = Path(__file__).resolve().parent

# Project root
PROJECT_DIRECTORY = BASE_DIRECTORY.parent

# Dataset folder
DATASET_DIRECTORY = PROJECT_DIRECTORY / "datasets"


# ==========================================================
# Master Dataset Files
# ==========================================================

CUSTOMERS_FILE = DATASET_DIRECTORY / "customers_master.csv"

PRODUCTS_FILE = DATASET_DIRECTORY / "products_master.csv"

SALESPERSONS_FILE = DATASET_DIRECTORY / "salespersons_master.csv"

REGIONS_FILE = DATASET_DIRECTORY / "regions_master.csv"


# ==========================================================
# Output Dataset
# ==========================================================

OUTPUT_FILE = DATASET_DIRECTORY / "sales_transactions.csv"


# ==========================================================
# Dataset Settings
# ==========================================================

START_DATE = "2022-01-01"

END_DATE = "2026-12-31"

TOTAL_TRANSACTIONS = 100000


# ==========================================================
# Pricing Settings
# ==========================================================

GST_PERCENT = 18

MAX_DISCOUNT = 10

PRICE_VARIATION = 0.05


# ==========================================================
# Payment Settings
# ==========================================================

PAYMENT_METHODS = [

    "NEFT",

    "RTGS",

    "Bank Transfer"

]

PAYMENT_STATUS = [

    "Paid",

    "Pending",

    "Partial"

]


# ==========================================================
# Delivery Settings
# ==========================================================

DELIVERY_MODES = [

    "Road",

    "Air",

    "Rail",

    "Sea"

]


# ==========================================================
# Random Seed
# ==========================================================

RANDOM_SEED = 42