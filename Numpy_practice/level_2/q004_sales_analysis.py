import numpy as np

sales = []
for i in range(1, 11):
    sales_amount = int(input(f"enter sales amount {i}: "))
    sales.append(sales_amount)

sales_array = np.array(sales)

greater_sales= sales_array[sales_array > 5000]
less_sales = sales_array[sales_array < 2000]
sales_range = sales_array[(sales_array >= 2000) & (sales_array <= 5000)]

print(f"Original sales: {sales_array}")
print(f"greater sales: {greater_sales}")
print(f"less sales: {less_sales}")
print(f"Sales between 2000 to 5000: {sales_range}")
print(f"greater sales count: {greater_sales.size}")
print(f"less sales count: {less_sales.size}")
print(f"Between 2k to 5k count: {sales_range.size}")




