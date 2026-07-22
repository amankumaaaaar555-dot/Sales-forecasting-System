"""
region_generator.py

Generate Region Master Dataset

Author: Aman Kumar
"""

import pandas as pd

# ==========================================================
# Regions
# ==========================================================

REGIONS = [

    ("REG001", "Rajasthan", "North"),
    ("REG002", "Gujarat", "West"),
    ("REG003", "Delhi NCR", "North"),
    ("REG004", "Haryana", "North"),
    ("REG005", "Punjab", "North"),
    ("REG006", "Uttar Pradesh", "North"),
    ("REG007", "Maharashtra", "West"),
    ("REG008", "Madhya Pradesh", "Central"),
    ("REG009", "Tamil Nadu", "South"),
    ("REG010", "Karnataka", "South"),
    ("REG011", "Andhra Pradesh", "South"),
    ("REG012", "Telangana", "South"),
    ("REG013", "Kerala", "South"),
    ("REG014", "Odisha", "East"),
    ("REG015", "West Bengal", "East"),
    ("REG016", "Assam", "East"),
    ("REG017", "Jharkhand", "East"),
    ("REG018", "Chhattisgarh", "Central"),
    ("REG019", "Bihar", "East"),
    ("REG020", "Goa", "West")

]


# ==========================================================
# Generate Regions
# ==========================================================

def generate_regions():

    data = []

    for region_id, region_name, zone in REGIONS:

        data.append({

            "Region_ID": region_id,

            "Region_Name": region_name,

            "Zone": zone,

            "Growth_Potential": "High",

            "Status": "Active"

        })

    return pd.DataFrame(data)


# ==========================================================
# Save
# ==========================================================

def save_regions():

    df = generate_regions()

    df.to_csv(

        "datasets/regions_master.csv",

        index=False

    )

    print(df.head())

    print()

    print("Total Regions :", len(df))


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    save_regions()