"""
product_generator.py

Generate Product Master Dataset

Author: Aman Kumar
"""

import random
import pandas as pd

random.seed(42)

# ==========================================================
# Product Names
# ==========================================================

PRODUCTS = [

    "Hydraulic Cylinder",
    "Bridge Plug",
    "Stabilizer",
    "Mud Motor",
    "Drill Collar",
    "Crossover",
    "Float Collar",
    "Float Shoe",
    "Centralizer",
    "Liner Hanger",
    "Packer",
    "Tubing Hanger",
    "Wellhead Assembly",
    "Christmas Tree",
    "Completion Valve",
    "Drill Bit",
    "Casing Pipe"

]

# ==========================================================
# Categories
# ==========================================================

CATEGORIES = [

    "Hydraulic Equipment",
    "Completion Tools",
    "Downhole Tools",
    "Drilling Tools",
    "Wellhead Equipment"

]

TOTAL_PRODUCTS = len(PRODUCTS)
# ==========================================================
# Generate Products
# ==========================================================

def generate_products():

    products = []

    for i, product_name in enumerate(PRODUCTS, start=1):

        manufacturing_cost = random.randint(300000, 1200000)

        selling_price = int(
            manufacturing_cost * random.uniform(1.20, 1.45)
        )

        product = {

            "Product_ID": f"PRD{i:04d}",

            "Product_Name": product_name,

            "Category": random.choice(CATEGORIES),

            "Manufacturing_Cost": manufacturing_cost,

            "Selling_Price": selling_price,

            "Lead_Time_Days": random.randint(5, 40),

            "Stock_Quantity": random.randint(50, 500),

            "Reorder_Level": random.randint(20, 100),

            "Demand_Level": random.choice(
                [
                    "Low",
                    "Medium",
                    "High"
                ]
            ),

            "Status": "Active"

        }

        products.append(product)

    return pd.DataFrame(products)


# ==========================================================
# Save CSV
# ==========================================================

def save_products():

    df = generate_products()

    df.to_csv(

        "datasets/products_master.csv",

        index=False

    )

    print()

    print("=" * 60)

    print("PRODUCT MASTER GENERATED SUCCESSFULLY")

    print("=" * 60)

    print()

    print(df.head())

    print()

    print("Total Products :", len(df))


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    save_products()