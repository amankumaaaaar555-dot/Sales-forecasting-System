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
# Dataset Configuration
# ==========================================================

DEFAULT_DATASET_NAME = "sales_transactions.csv"

DATE_COLUMN = "Invoice_Date"

TARGET_COLUMN = "Total_Amount"

DATE_FORMAT = "%Y-%m-%d"

# ==========================================================
# Dataset Schema
# ==========================================================

ID_COLUMNS = [

    "Invoice_Number",

    "Customer_ID",

    "Salesperson_ID",

    "Product_ID",

    "Region_ID"

]

CATEGORICAL_COLUMNS = [

    "Customer_Name",

    "Customer_Type",

    "Industry",

    "Region_Name",

    "Zone",

    "Salesperson_Name",

    "Designation",

    "Product_Name",

    "Category",

    "Payment_Method",

    "Payment_Status",

    "Delivery_Status",

    "Demand_Level",

    "Weekday"

]

NUMERICAL_COLUMNS = [

    "Year",

    "Month",

    "Quarter",

    "Day",

    "Quantity",

    "Manufacturing_Cost",

    "Selling_Price",

    "Subtotal",

    "Discount_Percent",

    "Discount_Amount",

    "GST",

    "Profit",

    "Lead_Time_Days"

]

# ==========================================================
# Model Configuration
# ==========================================================

RANDOM_STATE = 42

TEST_SIZE = 0.20

# ==========================================================
# Forecast Configuration
# ==========================================================

# D = Daily
# W = Weekly
# M = Monthly

FORECAST_FREQUENCY = "D"

DEFAULT_FORECAST_HORIZON = 30

DEFAULT_SPLIT_METHOD = "Time Series"