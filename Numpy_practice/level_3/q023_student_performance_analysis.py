import numpy as np
import pandas as pd


def attendance_warning(attendance):
    if attendance < 75:
        return "Warning"
    return "Good"


def classify_student(average):
    if average >= 85:
        return "Excellent"
    if average >= 70:
        return "Good"
    if average >= 50:
        return "Average"
    return "Needs Improvement"


df = pd.read_csv("files/students.csv")

# Calculate average marks
df["Average"] = (
    df[["Math", "Science", "English"]]
    .mean(axis=1)
    .round(2)
)

# High-performing students
high_performing_students = df[
    (df["Average"] >= 80) &
    (df["Attendance"] >= 90)
][["Name", "City", "Average", "Attendance"]]

# NumPy analysis
average_array = df["Average"].to_numpy()

overall_average = average_array.mean()
highest_average = average_array.max()
lowest_average = average_array.min()

difference = np.abs(average_array - overall_average)

highest_average_index = np.argmax(average_array)
top_student = df.iloc[highest_average_index]

# City analysis
citywise_average = df.groupby("City")["Average"].mean().round(2)

best_performing_city = citywise_average.idxmax()
best_city_average = citywise_average.max()

# Attendance status
df["Attendance Status"] = df["Attendance"].apply(attendance_warning)

# Performance classification
df["Performance"] = df["Average"].apply(classify_student)

# Counts
performance_counts = df["Performance"].value_counts()
attendance_counts = df["Attendance Status"].value_counts()

warning_count = attendance_counts.get("Warning", 0)

# Final report
print(f"High-performing students:\n{high_performing_students}")

print(f"\nOverall average: {overall_average:.2f}")
print(f"Highest average: {highest_average:.2f}")
print(f"Lowest average: {lowest_average:.2f}")

print(f"\nDifference from overall average:\n{difference}")

print(f"\nTop student:\n{top_student}")

print(f"\nBest-performing city: {best_performing_city}")
print(f"Best city average: {best_city_average:.2f}")

print(f"\nUpdated DataFrame:\n{df}")

print(f"\nPerformance category counts:\n{performance_counts}")

print(f"\nStudents with attendance warning: {warning_count}")