"""
business_rules.py

Business Rules for Enterprise Sales Dataset

Author: Aman Kumar
"""

import random
from datetime import datetime, timedelta

# ==========================================================
# Random Seed
# ==========================================================

random.seed(42)

# ==========================================================
# Invoice Number
# ==========================================================

_invoice_counter = 100000

def generate_invoice_number():
    global _invoice_counter
    _invoice_counter += 1
    return f"INV{_invoice_counter}"

# ==========================================================
# Invoice Date
# ==========================================================

START_DATE = datetime(2022, 1, 1)
END_DATE = datetime(2025, 12, 31)

def generate_invoice_date():

    days = (END_DATE - START_DATE).days

    return START_DATE + timedelta(
        days=random.randint(0, days)
    )

# ==========================================================
# Quantity
# ==========================================================

def generate_quantity():

    return random.randint(1, 25)

# ==========================================================
# Discount
# ==========================================================

def generate_discount():

    return random.choice(
        [0, 5, 10, 15, 20]
    )
# ==========================================================
# GST
# ==========================================================

GST_RATE = 0.18

def calculate_gst(amount):

    return round(amount * GST_RATE, 2)


# ==========================================================
# Profit
# ==========================================================

def calculate_profit(cost, selling_price, quantity):

    return round(
        (selling_price - cost) * quantity,
        2
    )


# ==========================================================
# Payment Method
# ==========================================================

PAYMENT_METHODS = [

    "Cash",
    "UPI",
    "Bank Transfer",
    "RTGS",
    "NEFT",
    "Cheque"

]

def generate_payment_method():

    return random.choice(
        PAYMENT_METHODS
    )


# ==========================================================
# Payment Status
# ==========================================================

PAYMENT_STATUS = [

    "Paid",
    "Pending",
    "Overdue"

]

def generate_payment_status():

    return random.choice(
        PAYMENT_STATUS
    )


# ==========================================================
# Delivery Status
# ==========================================================

DELIVERY_STATUS = [

    "Delivered",
    "In Transit",
    "Processing"

]

def generate_delivery_status():

    return random.choice(
        DELIVERY_STATUS
    )
# ==========================================================
# Year
# ==========================================================

def get_year(date):

    return date.year


# ==========================================================
# Month
# ==========================================================

def get_month(date):

    return date.month


# ==========================================================
# Quarter
# ==========================================================

def get_quarter(date):

    return ((date.month - 1) // 3) + 1


# ==========================================================
# Day
# ==========================================================

def get_day(date):

    return date.day


# ==========================================================
# Weekday
# ==========================================================

def get_weekday(date):

    return date.strftime("%A")


# ==========================================================
# Month Name
# ==========================================================

def get_month_name(date):

    return date.strftime("%B")


# ==========================================================
# Financial Quarter
# ==========================================================

def get_financial_quarter(date):

    month = date.month

    if month in [4, 5, 6]:
        return "Q1"

    elif month in [7, 8, 9]:
        return "Q2"

    elif month in [10, 11, 12]:
        return "Q3"

    else:
        return "Q4"