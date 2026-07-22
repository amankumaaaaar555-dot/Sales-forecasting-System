"""
customer_generator.py

Generate Customer Master Dataset

Author: Aman Kumar
"""

import random
import pandas as pd

random.seed(42)

# ==========================================================
# Region Mapping
# ==========================================================

REGIONS = [

    ("REG001", "Rajasthan"),
    ("REG002", "Gujarat"),
    ("REG003", "Delhi NCR"),
    ("REG004", "Haryana"),
    ("REG005", "Punjab"),
    ("REG006", "Uttar Pradesh"),
    ("REG007", "Maharashtra"),
    ("REG008", "Madhya Pradesh"),
    ("REG009", "Tamil Nadu"),
    ("REG010", "Karnataka"),
    ("REG011", "Andhra Pradesh"),
    ("REG012", "Telangana"),
    ("REG013", "Kerala"),
    ("REG014", "Odisha"),
    ("REG015", "West Bengal"),
    ("REG016", "Assam"),
    ("REG017", "Jharkhand"),
    ("REG018", "Chhattisgarh"),
    ("REG019", "Bihar"),
    ("REG020", "Goa")

]

# ==========================================================
# Company Names
# ==========================================================

COMPANIES = [

    "Reliance Industries",
    "Indian Oil",
    "ONGC",
    "Bharat Petroleum",
    "HPCL",
    "Vedanta Limited",
    "Cairn Oil",
    "Essar Oil",
    "GAIL India",
    "Oil India",
    "Larsen & Toubro",
    "Tata Steel",
    "JSW Steel",
    "Adani Power",
    "NTPC",
    "BHEL",
    "Engineers India",
    "Schlumberger",
    "Halliburton",
    "Baker Hughes"

]

# ==========================================================
# Industry Types
# ==========================================================

INDUSTRIES = [

    "Oil & Gas",
    "Manufacturing",
    "Energy",
    "Mining",
    "Engineering"

]

# ==========================================================
# Customer Types
# ==========================================================

CUSTOMER_TYPES = [

    "Silver",
    "Gold",
    "Platinum"

]
# ==========================================================
# Generate Customers
# ==========================================================

TOTAL_CUSTOMERS = 500

def generate_customers():

    customers = []

    for i in range(1, TOTAL_CUSTOMERS + 1):

        region = random.choice(REGIONS)

        company = random.choice(COMPANIES)

        customer = {

            "Customer_ID": f"CUST{i:04d}",

            "Customer_Name": f"{company} Branch {random.randint(1,30)}",

            "Region_ID": region[0],

            "Region_Name": region[1],

            "Industry": random.choice(INDUSTRIES),

            "Customer_Type": random.choice(CUSTOMER_TYPES),

            "Status": "Active"

        }

        customers.append(customer)

    return pd.DataFrame(customers)


# ==========================================================
# Save CSV
# ==========================================================

def save_customers():

    df = generate_customers()

    df.to_csv(

        "datasets/customers_master.csv",

        index=False

    )

    print()

    print("=" * 60)

    print("CUSTOMER MASTER GENERATED SUCCESSFULLY")

    print("=" * 60)

    print()

    print(df.head())

    print()

    print("Total Customers :", len(df))


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    save_customers()