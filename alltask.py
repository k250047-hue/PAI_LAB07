import pandas as pd

data = pd.read_csv("customers.csv")

# task1
print("Dataset Shape:")
print(data.shape)

print("\nData Types:")
print(data.dtypes)

print("\nMissing Values:")
print(data.isnull().sum())


# task2
data.dropna(subset=["Customer_ID"], inplace=True)

print("\nAfter Removing Missing Customer IDs:")
print(data.shape)


# task3
data["Age"] = data["Age"].fillna(data["Age"].median())

data["Total_Spent"] = data["Total_Spent"].fillna(data["Total_Spent"].mean())

print("\nMissing Values After Imputation:")
print(data[["Age", "Total_Spent"]].isnull().sum())


# task4
data["Join_Date"] = pd.to_datetime(data["Join_Date"])

data["Join_Year"] = data["Join_Date"].dt.year

data["Join_Month"] = data["Join_Date"].dt.month_name()

print("\nJoin Year and Month:")
print(data[["Join_Date", "Join_Year", "Join_Month"]])


# task5
data["Avg_Order_Value"] = data["Total_Spent"] / data["Order_Count"]

print("\nAverage Order Value:")
print(data[["Customer_ID", "Avg_Order_Value"]])


# task6
data["High_Value_Customer"] = data["Avg_Order_Value"] > 2500

print("\nHigh Value Customers:")
print(data[["Customer_ID", "High_Value_Customer"]])


# task7
city_analysis = data.groupby("City").agg(
    Total_Customers=("Customer_ID", "count"),
    Average_Spending=("Total_Spent", "mean"),
    Maximum_Orders=("Order_Count", "max")
)

print("\nCity Analysis:")
print(city_analysis)


# task8
vip_analysis = pd.pivot_table(
    data,
    index="Category",
    columns="Is_VIP",
    values="Total_Spent",
    aggfunc="sum",
    fill_value=0
)

print("\nRevenue by Category and VIP Status:")
print(vip_analysis)


# task9
top_customers = data[data["Category"].isin(["Electronics", "Clothing"])]

top_customers = top_customers.sort_values(
    by="Total_Spent",
    ascending=False
).head(5)

print("\nTop 5 Customers:")
print(top_customers[["Customer_ID", "Category", "Total_Spent"]])


# task10
vip_customers = data[data["Is_VIP"] == True]

karachi_vip = vip_customers[vip_customers["City"] == "Karachi"]

lahore_vip = vip_customers[vip_customers["City"] == "Lahore"]

print("\nAverage Order Count of Karachi VIP Customers:")
print(karachi_vip["Order_Count"].mean())

print("\nAverage Order Count of Lahore VIP Customers:")
print(lahore_vip["Order_Count"].mean())


# task11
print("\nThree Key Analytical Insights:")

print("1. City-wise customer spending can be compared using the city analysis.")

print("2. VIP and non-VIP revenue can be compared using the pivot table.")

print("3. High-value customers can be identified using Avg_Order_Value greater than 2500.")