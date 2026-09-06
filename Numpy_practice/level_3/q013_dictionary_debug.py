sales = {
    "Arun": [1000, 1500, 2000],
    "Bala": [1200, 1800],
    "Cathy": [2000, 2500, 1000]
}

for employee in sales:
    total = sum(sales[employee])
    print(employee, total)