# A delivery company records the distances traveled by 10 vehicles, in kilometers:

# distances = np.array([12, -8, 25, 15, -20, 30, 7, -5, 18, 22])

# The negative values represent distances recorded in the wrong direction and should be treated as positive distances.

# Write a program that prints:

# Original distances.
# Corrected distances, where negative values become positive.
# The average corrected distance.
# The shortest corrected distance.
# The longest corrected distance.
# All corrected distances greater than the average.
# The corrected distances at indexes 1, 3, 5, and 8.
# A new array containing the corrected distances with 5 km added to every value.

import numpy as np

distances = np.array([12, -8, 25, 15, -20, 30, 7, -5, 18, 22])

corrected_distances = np.abs(distances)
distnaces_average = np.mean(corrected_distances)

shortest_distance = np.min(corrected_distances)
longest_distance = np.max(corrected_distances)

greater_than_average = corrected_distances[corrected_distances > distnaces_average]
distances_with_5km_added = corrected_distances + 5

print(f"Original Distances: {distances}")
print(f"Corrected distances: {corrected_distances}")
print(f"The average corrected distance: {distnaces_average}")
print(f"The shortest corrected distance: {shortest_distance}")
print(f"The longest corrected distance: {longest_distance}")
print(f"All corrected distances greater than the average: {greater_than_average}")
print(f"The corrected distances at indexes 1, 3, 5, and 8: {corrected_distances[[1, 3, 5, 8]]}")
print(f"the corrected distances with 5 km added: {distances_with_5km_added}")