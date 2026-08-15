# A company has recorded the monthly sales of 12 employees.

# Ask the user to enter the sales amount for each employee.

# Then create a NumPy array and print:

# Original sales.
# Sales above ₹50,000.
# Sales between ₹30,000 and ₹50,000 inclusive.
# Sales below ₹30,000.
# Number of employees in each category.
# Create a new array containing only the sales above ₹50,000.
# Calculate a 10% bonus for those high-performing employees.

import numpy as np

monthly_sales = []
for i in range(1,13):
    sales = int(input(f"Enter Monthly Sales of Employee {i}: "))
    monthly_sales.append(sales)

sales_record_array = np.array(monthly_sales)
high_sales = sales_record_array[sales_record_array > 50000]
average_sales = sales_record_array[(sales_record_array >= 30000) & (sales_record_array <= 50000)]
low_sales = sales_record_array[sales_record_array < 30000]
bonus = high_sales * 0.10

print(f"Original Sales: {sales_record_array}")
print(f"High Sales: {high_sales}")
print(f"Average Sales: {average_sales}")
print(f"Low Sales: {low_sales}")

print(f"""
High sales Employee Count: {high_sales.size}
Average Sales Employee Count: {average_sales.size}
Low Sales Employee Count: {low_sales.size}""")

print(f"Bonus for High-Performing Employee: {bonus}")


