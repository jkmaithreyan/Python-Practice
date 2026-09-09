import numpy as np
import pandas as pd


def classify_member(visits):
    if visits >= 20:
        return "Very Active"
    if visits >= 12:
        return "Active"
    if visits >= 6:
        return "Regular"
    return "Low Activity"


def calculate_discount(visits, monthly_fee):
    if visits >= 20:
        return monthly_fee * 0.15
    if visits >= 12:
        return monthly_fee * 0.10
    return 0


try:
    df = pd.read_csv("files/members.csv")

except FileNotFoundError:
    print("Error: files/members.csv was not found.")

else:
    # Calculate annual values
    df["AnnualFee"] = df["MonthlyFee"] * 12
    df["AnnualCalories"] = df["CaloriesBurned"] * 12

    # Highly active members
    highly_active = df[
        (df["Visits"] >= 15) &
        (df["CaloriesBurned"] >= 6000)
    ][["Name", "Plan", "Visits", "CaloriesBurned"]]

    # NumPy visit analysis
    visits = df["Visits"].to_numpy()

    total_visits = visits.sum()
    average_visits = visits.mean()
    minimum_visits = visits.min()
    maximum_visits = visits.max()

    visit_difference = np.abs(visits - average_visits)

    max_visit_index = np.argmax(visits)
    most_active_member = df.iloc[max_visit_index]

    # Plan activity analysis
    average_visits_by_plan = (
        df.groupby("Plan")["Visits"]
        .mean()
        .round(2)
    )

    most_active_plan = average_visits_by_plan.idxmax()
    most_active_plan_average = average_visits_by_plan.max()

    # Highest-rated member
    highest_rating_index = df["Rating"].idxmax()

    highest_rated_member = df.loc[
        highest_rating_index,
        ["Name", "Plan", "Rating", "Visits"]
    ]

    # Activity classification
    df["Activity_Category"] = df["Visits"].apply(classify_member)

    # Loyalty discounts
    df["Discount"] = df.apply(
        lambda row: calculate_discount(
            row["Visits"],
            row["MonthlyFee"]
        ),
        axis=1
    )

    df["NextMonthFee"] = df["MonthlyFee"] - df["Discount"]

    # Revenue analysis
    current_monthly_revenue = df["MonthlyFee"].sum()
    next_month_revenue = df["NextMonthFee"].sum()
    total_discount = df["Discount"].sum()

    # Activity category counts
    activity_counts = df["Activity_Category"].value_counts()

    # Revenue by plan
    revenue_by_plan = df.groupby("Plan")["MonthlyFee"].sum()

    highest_revenue_plan = revenue_by_plan.idxmax()
    highest_plan_revenue = revenue_by_plan.max()

    # Final report
    print(f"Highly active members:\n{highly_active}")

    print(f"\nTotal visits: {total_visits}")
    print(f"Average visits: {average_visits:.2f}")
    print(f"Minimum visits: {minimum_visits}")
    print(f"Maximum visits: {maximum_visits}")

    print(
        f"\nDifference from average visits:\n"
        f"{visit_difference}"
    )

    print(
        f"\nMember with maximum visits:\n"
        f"{most_active_member}"
    )

    print(
        f"\nAverage visits by plan:\n"
        f"{average_visits_by_plan}"
    )

    print(
        f"\nMost active plan: {most_active_plan}"
        f"\nAverage visits: {most_active_plan_average:.2f}"
    )

    print(f"\nHighest-rated member:\n{highest_rated_member}")

    print(f"\nUpdated DataFrame:\n{df}")

    print(f"\nCurrent monthly revenue: ₹{current_monthly_revenue}")
    print(f"Next-month revenue: ₹{next_month_revenue}")
    print(f"Total discount given: ₹{total_discount}")

    print(
        f"\nActivity category counts:\n"
        f"{activity_counts}"
    )

    print(
        f"\nPlan with highest monthly revenue: "
        f"{highest_revenue_plan}"
    )

    print(f"Revenue: ₹{highest_plan_revenue}")