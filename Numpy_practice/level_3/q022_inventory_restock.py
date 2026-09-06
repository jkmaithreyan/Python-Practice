# The shop wants to add 10 units only to products whose stock is below 10.

# Your tasks
# Find the products with stock below 10.
# Add 10 to those products in the original stock array.
# Print the final stock array.
# Print the total stock after restocking.

import numpy as np

stock = np.array([12, 5, 28, 8, 15, 3, 20, 7])

stock[stock < 10] += 10

print(stock)
print(stock.sum())