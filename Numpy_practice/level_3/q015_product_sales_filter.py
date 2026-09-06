# A manager wants to know:

# Which products generated more than ₹10,000 in revenue per row?

# Your task
# Create a Revenue column.
# Filter the rows where Revenue > 10000.
# Print only:
# Product
# Revenue

import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Mouse", "Laptop"],
    "Quantity": [2, 10, 5, 3, 8, 4],
    "Price": [50000, 800, 1500, 12000, 800, 50000]
}

df = pd.DataFrame(data)

df["Revenue"] = df["Quantity"] * df["Price"]
higher_revenue = df[df["Revenue"] > 10000]

print(higher_revenue[["Product", "Revenue"]])

