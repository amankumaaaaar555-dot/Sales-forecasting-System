"""
transaction_generator.py

Enterprise Sales Transaction Generator

Author: Aman Kumar
"""

# ==========================================================
# Imports
# ==========================================================

import random
import pandas as pd

from business_rules import (
    generate_invoice_number,
    generate_invoice_date,
    generate_quantity,
    generate_discount,
    calculate_gst,
    calculate_profit,
    generate_payment_method,
    generate_payment_status,
    generate_delivery_status,
    get_year,
    get_month,
    get_quarter,
    get_day,
    get_weekday
)

# ==========================================================
# Configuration
# ==========================================================

TOTAL_TRANSACTIONS = 100

CUSTOMERS_FILE = "datasets/customers_master.csv"
PRODUCTS_FILE = "datasets/products_master.csv"
SALESPERSONS_FILE = "datasets/salespersons_master.csv"
REGIONS_FILE = "datasets/regions_master.csv"

OUTPUT_FILE = "datasets/sales_transactions.csv"

random.seed(42)

# ==========================================================
# Load Master Data
# ==========================================================

def load_master_data():

    customers = pd.read_csv(CUSTOMERS_FILE)

    products = pd.read_csv(PRODUCTS_FILE)

    salespersons = pd.read_csv(SALESPERSONS_FILE)

    regions = pd.read_csv(REGIONS_FILE)

    return (
        customers,
        products,
        salespersons,
        regions
    )

# ==========================================================
# Generate One Transaction
# ==========================================================

def generate_single_transaction(
    customers,
    products,
    salespersons,
    regions
):
        # ------------------------------------------------------
    # Select Customer
    # ------------------------------------------------------

    customer = customers.sample(1).iloc[0]

    # ------------------------------------------------------
    # Select Salesperson (Prefer Same Region)
    # ------------------------------------------------------

    matching_salespersons = salespersons[
        salespersons["Region_ID"] == customer["Region_ID"]
    ]

    if len(matching_salespersons) > 0:

        salesperson = matching_salespersons.sample(1).iloc[0]

    else:

        salesperson = salespersons.sample(1).iloc[0]

    # ------------------------------------------------------
    # Select Product
    # ------------------------------------------------------

    product = products.sample(1).iloc[0]

    # ------------------------------------------------------
    # Generate Business Values
    # ------------------------------------------------------

    invoice_number = generate_invoice_number()

    invoice_date = generate_invoice_date()

    quantity = generate_quantity()

    discount_percent = generate_discount()

    manufacturing_cost = product["Manufacturing_Cost"]

    selling_price = product["Selling_Price"]

    subtotal = quantity * selling_price

    discount_amount = subtotal * discount_percent / 100

    taxable_amount = subtotal - discount_amount

    gst = calculate_gst(taxable_amount)

    total_amount = taxable_amount + gst

    profit = calculate_profit(
        manufacturing_cost,
        selling_price,
        quantity
    )

    # ------------------------------------------------------
    # Region Details
    # ------------------------------------------------------

    region = regions[
        regions["Region_ID"] == customer["Region_ID"]
    ].iloc[0]

    # ------------------------------------------------------
    # Create Transaction Dictionary
    # ------------------------------------------------------

    transaction = {

        "Invoice_Number": invoice_number,

        "Invoice_Date": invoice_date.strftime("%Y-%m-%d"),

        "Year": get_year(invoice_date),

        "Month": get_month(invoice_date),

        "Quarter": get_quarter(invoice_date),

        "Day": get_day(invoice_date),

        "Weekday": get_weekday(invoice_date),

        "Customer_ID": customer["Customer_ID"],

        "Customer_Name": customer["Customer_Name"],

        "Customer_Type": customer["Customer_Type"],

        "Industry": customer["Industry"],

        "Region_ID": customer["Region_ID"],

        "Region_Name": customer["Region_Name"],

        "Zone": region["Zone"],

        "Salesperson_ID": salesperson["Salesperson_ID"],

        "Salesperson_Name": salesperson["Salesperson_Name"],

        "Designation": salesperson["Designation"],

        "Product_ID": product["Product_ID"],

        "Product_Name": product["Product_Name"],

        "Category": product["Category"],

        "Quantity": quantity,

        "Manufacturing_Cost": manufacturing_cost,

        "Selling_Price": selling_price,

        "Subtotal": round(subtotal, 2),

        "Discount_Percent": discount_percent,

        "Discount_Amount": round(discount_amount, 2),

        "GST": round(gst, 2),

        "Profit": round(profit, 2),

        "Total_Amount": round(total_amount, 2),

        "Payment_Method": generate_payment_method(),

        "Payment_Status": generate_payment_status(),

        "Delivery_Status": generate_delivery_status(),

        "Lead_Time_Days": product["Lead_Time_Days"],

        "Demand_Level": product["Demand_Level"]

    }

    return transaction
# ==========================================================
# Generate Multiple Transactions
# ==========================================================

def generate_transactions(total_transactions=TOTAL_TRANSACTIONS):

    customers, products, salespersons, regions = load_master_data()

    transactions = []

    print("\nGenerating Transactions...\n")

    for i in range(total_transactions):

        transaction = generate_single_transaction(
            customers,
            products,
            salespersons,
            regions
        )

        transactions.append(transaction)

        # Progress update every 10 records
        if (i + 1) % 10 == 0:

            print(f"{i + 1} Transactions Generated...")

    return pd.DataFrame(transactions)


# ==========================================================
# Save Dataset
# ==========================================================

def save_transactions():

    df = generate_transactions()

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print()

    print("=" * 60)
    print("ENTERPRISE SALES DATASET GENERATED SUCCESSFULLY")
    print("=" * 60)
    print()

    print(f"Total Transactions : {len(df)}")
    print(f"Columns            : {len(df.columns)}")
    print()
    print(f"Saved File : {OUTPUT_FILE}")
    print()
    print(df.head())
    # ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    save_transactions()
