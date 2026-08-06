import numpy as np
temperature = []

for i in range(1, 8):
    enter_temp = int(input(f"enter temperature {i} in celsius: "))
    temperature.append(enter_temp)

original_temperatures = np.array(temperature)
hot_days = original_temperatures[original_temperatures >= 30]
cool_days = original_temperatures[original_temperatures < 30]
print(f"Original temperatures:{original_temperatures}")
print(f"hot days: {hot_days}")
print(f"cool days: {cool_days}")
print(f"hot days count: {hot_days.size}")
print(f"cool days count: {cool_days.size}")