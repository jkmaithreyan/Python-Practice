import pandas as pd
import numpy as np

df = pd.read_csv("files/sales.csv")

df["Revenue"] = df["Quantity"] * df["Price"]

high_value = df[df["Revenue"] >= 20000]

high_value_revenue_array = np.array(high_value["Revenue"])

#calculate total revenue from np array
total_revenue = high_value_revenue_array.sum()

#calculate average revenue
average_revenue = high_value_revenue_array.mean()

#calculate maximum revenue
highest_revenue = high_value_revenue_array.max()

#absulute Difference between actual revenue and average revenue
difference = abs(high_value_revenue_array - average_revenue)

#find the best performing city
#grouping by city with total revenue
citywise_revenue = df.groupby("City")["Revenue"].sum()

#determine which city is Highest total Revenue
high_revenue_city = citywise_revenue.idxmax()
high_city_revenue = citywise_revenue.max()

#Apply a restocking/business rule
df.loc[df["Quantity"] < 5, "Quantity"] += 2

#calculating average with updated df
df["Revenue"] = df["Price"] * df["Quantity"]

#Creating an order classification function
def classify_order(revenue):
    if revenue >= 50000:
        return "High"
    elif revenue >= 20000:
        return "Medium"
    else:
        return "Low"

df["Category"] = df["Revenue"].apply(classify_order)

revenue = df["Revenue"].sum()
avg_revenue = df["Revenue"].mean()

#count of category
count = df.groupby("Category").size()




print(f"High_value_Details\n{high_value[["OrderID", "Product", "Revenue"]]}")
print(f"\nhigh_value_revenue_array\n{high_value_revenue_array}")
print(f"\ntotal revenue from np array\n{total_revenue}")
print(f"\naverage revenue from np array\n{average_revenue}")
print(f"\nmaximum revenue\n{highest_revenue}")
print(f"\nDifference between actual revenue and average revenue\n{difference}")
print(f"\nBest performing city: {high_revenue_city} {high_city_revenue}")


print(f"\nUpdated Dataframe\n{df}")
print(f"\nTotal Revenue using updated df\n{revenue}")
print(f"\nAverage revenue using updated df\n{avg_revenue}")
print("\nHigh orders:", count["High"])
print("\nMedium orders:", count["Medium"])
print("\nLow orders:", count["Low"])