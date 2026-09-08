import numpy as np
import pandas as pd


def borrowing_status(days_borrowed):
    if days_borrowed <= 10:
        return "On Time"
    return "Late"


def fine_adjustment(fine):
    if fine >= 80:
        return fine - 20
    return fine


try:
    df = pd.read_csv("files/library.csv")

except FileNotFoundError:
    print("Error: files/library.csv was not found.")

else:

    # Borrowing status
    df["Borrowing_Status"] = df["DaysBorrowed"].apply(borrowing_status)

    # Late borrower analysis
    late_borrowers = df[
        (df["DaysBorrowed"] > 10) &
        (df["Fine"] >= 40)
    ][
        ["Student", "Department", "Book", "DaysBorrowed", "Fine"]
    ]

    # NumPy analysis
    days_borrowed = df["DaysBorrowed"].to_numpy()

    total_days = days_borrowed.sum()
    average_days = days_borrowed.mean()
    minimum_days = days_borrowed.min()
    maximum_days = days_borrowed.max()

    difference_from_average = np.abs(
        days_borrowed - average_days
    )

    maximum_days_index = np.argmax(days_borrowed)

    max_borrower = df.iloc[maximum_days_index]


    # Book analysis

    average_rating_by_book = (
        df.groupby("Book")["Rating"]
        .mean()
        .round(2)
    )

    highest_rated_book = average_rating_by_book.idxmax()
    highest_book_rating = average_rating_by_book.max()


    # Department fine analysis

    department_fines = df.groupby("Department")["Fine"].sum()

    highest_fine_department = department_fines.idxmax()
    highest_department_fine = department_fines.max()


    # Fine adjustment

    df["Fine"] = df["Fine"].apply(fine_adjustment)

    new_total_fine = df["Fine"].sum()

    # Borrowing status counts
    status_counts = df["Borrowing_Status"].value_counts()

    on_time_count = status_counts.get("On Time", 0)
    late_count = status_counts.get("Late", 0)


    # Final report
    print(f"Late borrowers:\n{late_borrowers}")

    print(f"\nTotal days borrowed: {total_days}")
    print(f"Average borrowing days: {average_days:.2f}")
    print(f"Minimum borrowing days: {minimum_days}")
    print(f"Maximum borrowing days: {maximum_days}")

    print(
        f"\nDifference from average:\n"
        f"{difference_from_average}"
    )

    print(f"\nStudent with maximum borrowing days:")
    print(max_borrower)

    print(
        f"\nAverage rating for every book:\n"
        f"{average_rating_by_book}"
    )

    print(
        f"\nHighest-rated book: {highest_rated_book}"
        f"\nAverage rating: {highest_book_rating:.2f}"
    )

    print(
        f"\nTotal fine by department:\n"
        f"{department_fines}"
    )

    print(
        f"\nDepartment with highest total fine: "
        f"{highest_fine_department}"
    )

    print(
        f"Original highest department fine: "
        f"₹{highest_department_fine}"
    )

    print(f"\nUpdated DataFrame:\n{df}")

    print(f"\nNew total fine collected: ₹{new_total_fine}")

    print(f"\nOn Time borrowings: {on_time_count}")
    print(f"Late borrowings: {late_count}")