import numpy as np
marks = []

for i in range(1, 11):
    mark = int(input(f"enter marks {i}: "))
    marks.append(mark)

original_mark = np.array(marks)
pass_marks = original_mark[original_mark >= 50]
fail_mark = original_mark[original_mark < 50]
print(f"Original marks:{original_mark}")
print(f"pass mark: {pass_marks}")
print(f"fail mark: {fail_mark}")
print(f"passed student count: {pass_marks.size}")
print(f"failed student count: {fail_mark.size}")