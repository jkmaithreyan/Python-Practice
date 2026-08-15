import numpy as np

units_sold = []
for i in range(1, 9):
    units = int(input(f"enter units sold for product {i}: "))
    units_sold.append(units)

units_sold_array = np.array(units_sold)
high_sales = units_sold_array[units_sold_array > 50]
medium_sales = units_sold_array[(units_sold_array >= 20) & (units_sold_array <= 50)]
low_sales = units_sold_array[units_sold_array < 20]
total_unit_sold = np.sum(units_sold_array)

print(f"Original Sales Data: {units_sold_array}")
print(f"High sales: {high_sales}")
print(f"Medium sales: {medium_sales}")
print(f"Low sales: {low_sales}")

print(f"""
High Sales count: {high_sales.size}
Medium Sales count: {medium_sales.size}
Low Sales count: {low_sales.size}""")
print(f"total_unit_sold: {total_unit_sold}")
