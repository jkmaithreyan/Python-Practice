# Problem

# Create this NumPy array of product prices:

# prices = np.array([120, 250, 80, 450, 300, 150, 500, 200])

# Write a program that:

# Print the original prices.
# Create a new array containing the first 5 prices.
# Create a new array containing the last 3 prices.
# Select prices at indexes 0, 2, 4, and 6 using fancy indexing.
# Create a new array where every price has a 10% discount.
# Create another array where ₹50 is added to every original price.
# Print all the results.

import numpy as np

def price_discount_analysis(price_values):

    first_5_prices = price_values[:5]
    last_3_prices = price_values[-3:]
    discount_prices = price_values - (price_values * 0.10)
    added_50_prices = price_values + 50

    print(f"Original Prices: {price_values}")
    print(f"First 5 Prices: {first_5_prices}")
    print(f"Last 3 Prices: {last_3_prices}")
    print(f"prices at indexes 0, 2, 4, and 6 using: {price_values[[0,2,4,6]]}")
    print(f"10% Discount Prices: {discount_prices}")
    print(f"₹50 is added to original price: {added_50_prices}")


product_prices_array = np.array([120, 250, 80, 450, 300, 150, 500, 200])

price_discount_analysis(product_prices_array)