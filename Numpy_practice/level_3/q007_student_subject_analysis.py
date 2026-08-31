# Problem

# A teacher has recorded marks for 4 students across 3 subjects:

# marks = np.array([
#     [80, 70, 90],
#     [60, 85, 75],
#     [95, 90, 88],
#     [50, 65, 70]
# ])

# Each row represents one student.

# Each column represents one subject.

#              Math  Science  English
# Student 1      80      70       90
# Student 2      60      85       75
# Student 3      95      90       88
# Student 4      50      65       70

# Write a program that prints:

# The original marks array.
# The average mark of each student.
# The average mark of each subject.
# The highest mark in each subject.
# The lowest mark in each subject.
# The marks of the first two students using slicing.
# The marks of Math and English for all students using fancy indexing.

import numpy as np

marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88],
    [50, 65, 70]
])


average_of_students = np.mean(marks, axis=1)
average_of_subjects = np.mean(marks, axis=0)

Highest_mark_of_each_subject = np.max(marks, axis=0)
lowest_marks_of_each_subject = np.min(marks, axis=0)

print(f"Original Marks: {marks}")
print(f"average mark of each student: {average_of_students}")
print(f"average mark of each subject: {average_of_subjects}")
print(f"highest mark in each subject: {Highest_mark_of_each_subject}")
print(f"lowest mark in each subject: {lowest_marks_of_each_subject}")
print(f"Marks of first two students: {marks[0:2,:]}")
print(f"Marks of Math and English: {marks[: , [0, 2]]}")
