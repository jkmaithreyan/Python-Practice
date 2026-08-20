# Create this NumPy array of temperatures in Celsius:

# [18, 25, 30, 22, 35, 28, 15, 32]

# Write a program that:

# Print the original temperatures.
# Print the first 4 temperatures.
# Print the last 3 temperatures.
# Select temperatures at indexes 1, 3, 5, and 7 using fancy indexing.
# Convert the entire temperature array from Celsius to Fahrenheit using: 
# Fahrenheit = (Celsius × 9/5) + 32

import numpy as np

def temperature_conversion(array_values):

    print(f"Original Temperatures: {array_values}")
    print(f"First Four Temperatures: {array_values[:4]}")
    print(f"Last Three Temperatures: {array_values[-3:]}")
    print(f"Temperatures at indexes 1, 3, 5, and 7: {array_values[[1,3,5,7]]}")
    fahrenheit_array =(array_values * 9/5) + 32
    print(f"Celsius to Fahrenheit: {fahrenheit_array}")



celsius_values_array = np.array([18, 25, 30, 22, 35, 28, 15, 32])
temperature_conversion(celsius_values_array)