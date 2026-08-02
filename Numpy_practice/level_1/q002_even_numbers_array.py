import numpy as np

numbers = []
for i in range(1,7):
    num = int(input(f"enter number {i}: "))
    numbers.append(num)

arr = np.array(numbers)
print("array: ", arr)
print(arr[arr % 2 == 0])