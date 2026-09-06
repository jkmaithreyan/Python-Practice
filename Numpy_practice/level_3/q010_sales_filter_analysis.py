# Your task:

# Part 1

# Create a new column called Revenue.

# Revenue should be:

# Quantity × Price
# Part 2

# Find all rows where:

# City == "Chennai"
# Part 3

# From those Chennai rows, select only:

# Quantity
# Revenue
# Part 4

# Find the total Revenue for Chennai.

# Part 5

# Find the average Revenue for Chennai.

# Part 6

# Print the city, quantity, price, and revenue for the row with the highest Revenue in the entire DataFrame.

import pandas as pd

data = {
    "City": ["Chennai", "Bangalore", "Chennai", "Vellore", "Bangalore", "Chennai"],
    "Quantity": [10, 5, 8, 12, 7, 15],
    "Price": [200, 500, 150, 100, 400, 250]
}

df = pd.DataFrame(data)

df["revenue"] = df["Quantity"] * df["Price"]

chennai_row = df[df["City"] == "Chennai"]

hightest_index = df["revenue"].idxmax()

print(chennai_row[["Quantity", "revenue"]])
print(chennai_row["revenue"].sum())
print(chennai_row["revenue"].mean())
print(df.loc[hightest_index])