# A shop has recorded the prices of 8 products:

# prices = np.array([120, 250, 80, 450, 300, 150, 500, 200])

# Write a program that determines:

# The original prices.
# The average price of all products.
# The minimum price.
# The maximum price.
# All products costing more than the average price.
# The difference between each price and the average price, using absolute values.
# The 10% discounted price of every product.

import numpy as np

prices = np.array([120, 250, 80, 450, 300, 150, 500, 200])

average_price = np.mean(prices)
minimum_price = np.min(prices)
maximum_price = np.max(prices)
cost_more_than_avg = prices[prices > average_price]
differences = np.abs(prices - average_price)
discounted_price = prices - (prices * 0.10)

print(f"Original Prices: {prices}")
print(f"Average Price of all products: {average_price}")
print(f"Minimum Price: {minimum_price}")
print(f"Maximum Price: {maximum_price}")
print(f"Costing more than average prices: {cost_more_than_avg}")
print(f"Difference between original price and average price: {differences}")
print(f"Discounted Prices: {discounted_price}")