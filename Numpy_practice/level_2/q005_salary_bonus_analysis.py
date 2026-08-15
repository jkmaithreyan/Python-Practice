import numpy as np

salaries = []
for i in range(1, 9):
    salary = int(input(f"enter salary of employee {i}: "))
    salaries.append(salary)

salaries_array = np.array(salaries)
eligible_salaries = salaries_array[salaries_array < 30000]
bonus_amount = eligible_salaries * 0.10

print(f"Original Salaries: {salaries_array}")
print(f"Eligible Salaries: {eligible_salaries}")
print(f"Bonus Amounts: {bonus_amount}")