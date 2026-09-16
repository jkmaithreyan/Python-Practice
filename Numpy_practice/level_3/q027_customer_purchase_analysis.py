import pandas as pd
import numpy as np

def valuable_customer(df):
    valuable = df[
        (df["Orders"] >= 5) &
        (df["TotalSpent"] >= 8000) &
        (df["Satisfaction"] >= 4)
    ]
    return valuable[["Name", "City", "Orders", "TotalSpent", "Satisfaction"]]

#Customer classification function
def classify_customer(total_spent):
    if total_spent >= 15000:
        return "VIP"
    elif total_spent >= 8000:
        return "High Value"
    elif total_spent >= 4000:
        return "Regular"
    return "Low Value"

#Cashback system function
def cashback_system(total_spent):
    if total_spent >= 15000:
        return total_spent * 0.10
    elif total_spent >= 8000:
        return total_spent * 0.05
    return 0
    

try:
    df = pd.read_csv("Numpy_practice/files/customers.csv")
except FileNotFoundError:
    print("error: Customers.csv file is not found in files")
else:
    #Calculate Average Item and money spent per order
    df["AverageItemPerOrder"] = (df["ItemsPurchased"] / df["Orders"]).round(2)
    df["AverageSpendPerOrder"] = (df["TotalSpent"] / df["Orders"]).round(2)

    #converting totalspent into array
    total_spent_arr = df["TotalSpent"].to_numpy()

    #Array analysis
    total_spending = total_spent_arr.sum()
    average_spending = total_spent_arr.mean()
    minimum_spending = total_spent_arr.min()
    maximum_spending = total_spent_arr.max()
    difference = np.abs(total_spent_arr - average_spending)

    #Higest spending customer
    highest_spending_index = np.argmax(total_spent_arr)
    highest_spending_customer = df.iloc[highest_spending_index]

    #city analysis
    city_analysis = df.groupby("City").agg(
        citywise_total_spending = ("TotalSpent", "sum"),
        average_satisfaction = ("Satisfaction", "mean")
    )

    #Customer classification column creation
    df["Customer_Category"] = df["TotalSpent"].apply(classify_customer)


    #Cashback system column creation
    df["Cashback"] = df["TotalSpent"].apply(cashback_system)
    df["FinalSpent"] = (df["TotalSpent"] - df["Cashback"])

    #Customer category analysis
    Customer_category_count = df["Customer_Category"].value_counts()
    total_Cashback_to_each_category = df.groupby("Customer_Category")["Cashback"].sum()

    
    print(f"Valuable customers\n{valuable_customer(df)}")
    
    print(f"""\nSpending statistics:
    total spending: {total_spending}
    average spending: {average_spending}
    minimum spending: {minimum_spending}
    maximum spending: {maximum_spending}\n
    absolute difference of every customer's spending from the average:
    {difference}\n""")

    print(f"\nCustomer with highest spending\n{highest_spending_customer}")
    print(f"\nTotal spending by city\n{city_analysis['citywise_total_spending']}")

    print(f"""\ncity with the highest total spending : {city_analysis['citywise_total_spending'].idxmax()} - {city_analysis['citywise_total_spending'].max()}""")

    print(f"\nAverage satisfaction by city\n{city_analysis['average_satisfaction']}")
    print(f"\nHighest-satisfaction city\n{city_analysis['average_satisfaction'].idxmax()} - {city_analysis['average_satisfaction'].max()}")

    print(f"\nUpdated DataFrame\n{df}")

    print(f"\nCustomer category counts\n{Customer_category_count}")
    print(f"\nCashback by category\n{total_Cashback_to_each_category}")
    print(f"\nCategory receiving the highest cashback\n{total_Cashback_to_each_category.idxmax()} - {total_Cashback_to_each_category.max()}")

    print(f"\nTotal company spending: {df['TotalSpent'].sum()}")
    print(f"\nTotal cashback given: {df['Cashback'].sum()}")
    print(f"\nTotal final spending after cashback: {df['FinalSpent'].sum()}")