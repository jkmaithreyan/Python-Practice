# Write a program that:

# Finds the average score.
# Finds all scores above the average.
# Finds the highest score.
# Finds the index of the highest score.
# Adds 5 bonus points to only the scores below 50.
# Prints the final array.

import numpy as np

scores = np.array([45, 72, 88, 34, 91, 67, 50, 83])

average_score = np.average(scores)
scores_above_average = scores[scores > average_score]
highest_score = np.max(scores)
highest_index = np.argmax(scores)
scores[scores < 50] += 5



print(average_score)
print(scores_above_average)
print(highest_score)
print(highest_index)
print(scores)