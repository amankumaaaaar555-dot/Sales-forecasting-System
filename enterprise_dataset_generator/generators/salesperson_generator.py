"""
salesperson_generator.py

Generate Salesperson Master Dataset

Author: Aman Kumar
"""

import random
import pandas as pd

random.seed(42)

# ==========================================================
# Names
# ==========================================================

FIRST_NAMES = [

    "Amit",
    "Rahul",
    "Vikas",
    "Karan",
    "Ankit",
    "Rohit",
    "Sandeep",
    "Nikhil",
    "Pooja",
    "Priya",
    "Shreya",
    "Neha"

]

LAST_NAMES = [

    "Sharma",
    "Gupta",
    "Singh",
    "Kumar",
    "Patel",
    "Yadav",
    "Agarwal",
    "Verma"

]

# ==========================================================
# Designations
# ==========================================================

DESIGNATIONS = [

    "Sales Executive",
    "Senior Sales Executive",
    "Area Sales Manager",
    "Regional Sales Manager"

]

# ==========================================================
# Regions
# ==========================================================

REGIONS = [

    ("REG001","Rajasthan"),
    ("REG002","Gujarat"),
    ("REG003","Delhi NCR"),
    ("REG004","Haryana"),
    ("REG005","Punjab"),
    ("REG006","Uttar Pradesh"),
    ("REG007","Maharashtra"),
    ("REG008","Madhya Pradesh"),
    ("REG009","Tamil Nadu"),
    ("REG010","Karnataka"),
    ("REG011","Andhra Pradesh"),
    ("REG012","Telangana"),
    ("REG013","Kerala"),
    ("REG014","Odisha"),
    ("REG015","West Bengal"),
    ("REG016","Assam"),
    ("REG017","Jharkhand"),
    ("REG018","Chhattisgarh"),
    ("REG019","Bihar"),
    ("REG020","Goa")

]

TOTAL_SALESPERSONS = 100
# ==========================================================
# Generate Salespersons
# ==========================================================

def generate_salespersons():

    salespersons = []

    for i in range(1, TOTAL_SALESPERSONS + 1):

        first_name = random.choice(FIRST_NAMES)

        last_name = random.choice(LAST_NAMES)

        region = random.choice(REGIONS)

        email = (
            first_name.lower()
            + "."
            + last_name.lower()
            + "@wellrx.com"
        )

        salesperson = {

            "Salesperson_ID": f"SP{i:04d}",

            "Salesperson_Name": f"{first_name} {last_name}",

            "Region_ID": region[0],

            "Region_Name": region[1],

            "Designation": random.choice(DESIGNATIONS),

            "Experience_Years": random.randint(1, 20),

            "Annual_Target_INR": random.choice([
                25000000,
                50000000,
                75000000,
                100000000
            ]),

            "Email": email,

            "Status": "Active"

        }

        salespersons.append(salesperson)

    return pd.DataFrame(salespersons)


# ==========================================================
# Save CSV
# ==========================================================

def save_salespersons():

    df = generate_salespersons()

    df.to_csv(
        "datasets/salespersons_master.csv",
        index=False
    )

    print()

    print("=" * 60)
    print("SALESPERSON MASTER GENERATED SUCCESSFULLY")
    print("=" * 60)

    print()

    print(df.head())

    print()

    print("Total Salespersons :", len(df))


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    save_salespersons()