# A teacher has marks for 8 students:

# [45, 78, 92, 56, 88, 34, 76, 95]

# Write a program that:

# Creates this NumPy array.
# Prints the original array.
# Prints the marks of the first student.
# Prints the marks of the last student.
# Prints the marks of students at index 2 through index 5.
# Prints the marks of the last 3 students.

import numpy as np

def student_marks():
    marks_array = np.array([45, 78, 92, 56, 88, 34, 76, 95])

    print(f"Original Array: {marks_array}")
    print(f"First Student Mark: {marks_array[0]}")
    print(f"Last Student Mark: {marks_array[-1]}")
    print(f"Mark of Students From index 2 to 5: {marks_array[2:6]}")
    print(f"Last Three Students Marks: {marks_array[-3:]}")

student_marks()
    
