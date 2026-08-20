# Problem

# Create these two NumPy arrays:

# array_1 = np.array([10, 20, 30, 40, 50])
# array_2 = np.array([2, 4, 5, 8, 10])

# Print:

# Addition of the two arrays.
# Subtraction of array_2 from array_1.
# Multiplication of the two arrays.
# Division of array_1 by array_2.
# Multiply every value in array_1 by 10.
# Add 100 to every value in array_2.

import numpy as np

def array_operations(arr1, arr2):

    addition = arr1 + arr2
    print(f"Addition of array1 and array2: {addition}")

    subtraction = arr1 - arr2
    print(f"Subtraction of array2 from array1: {subtraction}")

    multiplication = arr1 * arr2
    print(f"Multiplication of the two arrays: {multiplication}")

    division = arr1 / arr2
    print(f"Division of array_1 by array_2: {division}")

    multiply_arr1_by_10 = arr1 * 10
    print(f"Multiply every value in array_1 by 10: {multiply_arr1_by_10}")

    add_100_to_arr2 = arr2 + 100
    print(f"Add 100 to every value in array_2: {add_100_to_arr2}")

array_1 = np.array([10, 20, 30, 40, 50])
array_2 = np.array([2, 4, 5, 8, 10])

array_operations(array_1, array_2)