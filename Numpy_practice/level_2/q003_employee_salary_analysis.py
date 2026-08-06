import numpy as np

employees_salaries = []
for i in range(1, 9):
    salaries = int(input(f"enter employee salary {i}: "))
    employees_salaries.append(salaries)

salaries_array = np.array(employees_salaries)

high_salary = salaries_array[salaries_array >= 30000]
low_salary = salaries_array[salaries_array < 30000]
inclusive = salaries_array[(salaries_array >= 30000) & (salaries_array <= 50000)]

print(f"Original salaries: {salaries_array}")
print(f"high salaries: {high_salary}")
print(f"low salaries: {low_salary}")
print(f"Between 30000 to 50000: {inclusive}")
print(f"high salary count: {high_salary.size}")
print(f"low salary count: {low_salary.size}")
print(f"Between 30k to 50k count: {inclusive.size}")




