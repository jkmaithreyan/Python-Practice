import numpy as np

marks = []

for i in range(1, 9):
    mark = int(input(f"Enter mark {i}: "))
    marks.append(mark)

marks_array = np.array(marks)

excellent_marks = marks_array[marks_array >= 80]
average_marks = marks_array[(marks_array >= 50) & (marks_array < 80)]
low_marks = marks_array[marks_array < 50]
percentage = excellent_marks.size / marks_array.size * 100

print(f"Original Marks: {marks_array}")
print(f"Excellent Marks: {excellent_marks}")
print(f"Average Marks: {average_marks}")
print(f"Low Marks: {low_marks}")

print(f"""
Excellent marks Count: {excellent_marks.size}
Average marks Count: {average_marks.size}
Low marks Count: {low_marks.size}""")

print(f"Excellent Percentage: {percentage}%")