import numpy as np
store_values = []
for i in range(1,6):
    number = int(input(f"enter number {i}: "))
    store_values.append(number)

arr = np.array(store_values)
print("array: ", arr)
print("shape: ", arr.shape)
print("size: ", arr.size)
print("Dimension: ", arr.ndim)
print("Datatype: ", arr.dtype)