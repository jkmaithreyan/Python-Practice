import numpy as np
import pandas as pd


def delivery_status(time):
    if time <= 40:
        return "Fast"
    if time <= 55:
        return "Normal"
    return "Slow"


def is_problematic(time, rating):
    return time > 50 and rating < 4


def calculate_delivery_charge(delivery_time):
    if delivery_time <= 30:
        return 20
    if delivery_time <= 45:
        return 40
    return 70


try:
    df = pd.read_csv("files/food_orders.csv")

except FileNotFoundError:
    print("Error: food_orders.csv was not found.")

else:
    # Order metrics
    df["AverageItemPrice"] = (
        df["OrderValue"] / df["Items"]
    ).round(2)

    df["DeliveryStatus"] = (
        df["DeliveryTime"].apply(delivery_status)
    )

    # Problematic orders
    problematic_mask = df.apply(
        lambda row: is_problematic(
            row["DeliveryTime"],
            row["Rating"]
        ),
        axis=1
    )

    problematic_orders = df.loc[
        problematic_mask,
        ["Customer", "City", "Restaurant",
         "DeliveryTime", "Rating"]
    ]

    # NumPy analysis
    order_values = df["OrderValue"].to_numpy()

    total_order_value = order_values.sum()
    average_order_value = order_values.mean()
    minimum_order_value = order_values.min()
    maximum_order_value = order_values.max()

    difference_from_average = np.abs(
        order_values - average_order_value
    )

    highest_value_index = np.argmax(order_values)
    highest_value_order = df.iloc[highest_value_index]

    # Restaurant analysis
    restaurant_analysis = df.groupby("Restaurant").agg(
        total_value=("OrderValue", "sum"),
        average_value=("OrderValue", "mean"),
        average_rating=("Rating", "mean")
    ).round(2)

    highest_value_restaurant = (
        restaurant_analysis["total_value"].idxmax()
    )

    highest_rated_restaurant = (
        restaurant_analysis["average_rating"].idxmax()
    )

    # City analysis
    orders_by_city = df["City"].value_counts()

    most_orders_city = orders_by_city.idxmax()
    most_orders_count = orders_by_city.max()

    average_delivery_by_city = (
        df.groupby("City")["DeliveryTime"].mean().round(2)
    )

    # Delivery charges
    df["DeliveryCharge"] = (
        df["DeliveryTime"].apply(calculate_delivery_charge)
    )

    df["FinalOrderValue"] = (
        df["OrderValue"] + df["DeliveryCharge"]
    )

    # Business analysis
    total_original_value = df["OrderValue"].sum()
    total_delivery_charges = df["DeliveryCharge"].sum()
    total_final_value = df["FinalOrderValue"].sum()

    delivery_status_counts = df["DeliveryStatus"].value_counts()

    order_value_by_status = (
        df.groupby("DeliveryStatus")["OrderValue"].sum()
    )

    highest_value_status = order_value_by_status.idxmax()
    highest_status_value = order_value_by_status.max()

    # Final report
    print(f"Problematic orders:\n{problematic_orders}")

    print(f"\nTotal order value: ₹{total_order_value}")
    print(f"Average order value: ₹{average_order_value:.2f}")
    print(f"Minimum order value: ₹{minimum_order_value}")
    print(f"Maximum order value: ₹{maximum_order_value}")

    print(f"\nDifference from average:\n{difference_from_average}")

    print(f"\nHighest-value order:\n{highest_value_order}")

    print(f"\nRestaurant analysis:\n{restaurant_analysis}")

    print(f"\nHighest-value restaurant: {highest_value_restaurant}")
    print(f"Highest-rated restaurant: {highest_rated_restaurant}")

    print(f"\nOrders by city:\n{orders_by_city}")
    print(f"City with most orders: {most_orders_city} - {most_orders_count}")

    print(f"\nAverage delivery time by city:\n{average_delivery_by_city}")

    print(f"\nUpdated DataFrame:\n{df}")

    print(f"\nTotal original order value: ₹{total_original_value}")
    print(f"Total delivery charges: ₹{total_delivery_charges}")
    print(f"Total final order value: ₹{total_final_value}")

    print(f"\nDelivery status counts:\n{delivery_status_counts}")
    print(f"\nOrder value by delivery status:\n{order_value_by_status}")

    print(
        f"\nStatus generating the highest order value: "
        f"{highest_value_status} - ₹{highest_status_value}"
    )