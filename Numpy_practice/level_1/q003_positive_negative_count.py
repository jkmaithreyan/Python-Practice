import numpy as np
numbers = []

for i in range(1, 9):
    num = int(input (f"Enter number {i}: "))
    numbers.append(num)

number_array = np.array(numbers)

positive = number_array[number_array > 0]
negative = number_array[number_array < 0]

print("Original Array: ",number_array)
print("Positive Numbers: ",positive)
print("Negative Numbers: ", negative)
print("Positive Count: ", positive.size)
print("Negative count: ", negative.size)
        