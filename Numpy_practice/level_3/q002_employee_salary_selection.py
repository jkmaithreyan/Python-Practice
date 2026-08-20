# Problem

# Create this NumPy array:

# [25000, 32000, 45000, 28000, 50000, 38000, 60000, 42000]

# Write a program that prints:

# The first 3 salaries.
# The last 4 salaries.
# Salaries from index 2 to index 6.
# Every second salary from index 0 to index 6.
# The salary at indexes 1, 3, 5, and 7.

import numpy as np

def employee_salary_selection(array_values):

    print(f"First Three Salaries: {array_values[0:3]}")
    print(f"Last Four Salaries: {array_values[-4:]}")
    print(f"Salaries From index 2 to 6: {array_values[2:7]}")
    print(f"Every Second Salaries from index 0 to 6: {array_values[0:7:2]}")
    print(f"salary at indexes 1, 3, 5, and 7: {array_values[[1,3,5,7]]}")



salary_array = np.array([25000, 32000, 45000, 28000, 50000, 38000, 60000, 42000])
employee_salary_selection(salary_array)