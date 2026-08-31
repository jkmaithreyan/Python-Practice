# Problem

# A company records the performance scores of 8 employees:

# scores = np.array([72, 45, 88, 91, 56, 34, 79, 63])

# Write a program that prints:

# Original scores
# Average score
# Highest score
# Lowest score
# Scores above the average
# The absolute difference between every score and the average
# Scores at indexes 1, 3, 5, and 7
# A new array where 5 points are added to every score
# A new array containing the squared value of every score

import numpy as np

scores = np.array([72, 45, 88, 91, 56, 34, 79, 63])

average_score = np.mean(scores)
highest_score = np.max(scores)
lowest_score = np.min(scores)
scores_above_average = scores[scores > average_score]
difference = np.abs(scores - average_score)
added_5points = scores + 5
squared_scores = np.square(scores)

print(f"Original Scores: {scores}")
print(f"Average score: {average_score}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
print(f"Scores above average: {scores_above_average}")
print(f"Difference between score and average score: {difference}")
print(f"Scores at indexes 1, 3, 5, and 7: {scores[[1,3,5,7]]}")
print(f"Added 5 points to all: {added_5points}")
print(f"Squared values: {squared_scores}")