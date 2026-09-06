# Write a program to:

# Find the total number of items in stock.
# Find the average stock.
# Find all products with stock below the average.
# Find the highest stock value.
# Find the index of the product with the highest stock.
# Add 10 units to only the products whose stock is below 10.

import numpy as np

stock = np.array([25, 8, 42, 15, 5, 30, 12, 50])

total_stock = stock.sum()
average = stock.mean()
stock_below_average = stock[stock < average]
highest_stock = stock.max()
highest_index = stock.argmax()
stock[stock < 10] += 10

print(total_stock)
print(average)
print(stock_below_average)
print(highest_stock)
print(highest_index)
print(stock)