import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import the dataset into a Pandas DataFrame
df = pd.read_csv(
    "https://raw.githubusercontent.com/alexeygrigorev/datasets/master/AB_NYC_2019.csv"
)

# 2. Explore the basic statistics of the dataset using the describe() method
print(df.describe())

# 3. Clean the dataset by removing unnecessary columns and filling in missing values
columns_to_drop = ["id", "name", "host_name", "last_review"]
df = df.drop(columns=columns_to_drop)
df = df.fillna(df.mean())

# 4. Visualize the distribution of prices using a histogram
plt.hist(df["price"], bins=50, range=(0, 1000))
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Price Distribution")
plt.show()

# 5. Identify the top 10 neighborhoods with the highest number of listings and create a bar chart to visualize the results
top_neighborhoods = df["neighbourhood"].value_counts().head(10)
top_neighborhoods.plot(kind="bar")
plt.xlabel("Neighbourhood")
plt.ylabel("Number of Listings")
plt.title("Top 10 Neighbourhoods by Listings")
plt.show()

# 6. Analyze the relationship between price and availability by creating a scatter plot
plt.scatter(df["price"], df["availability_365"], alpha=0.1)
plt.xlabel("Price")
plt.ylabel("Availability")
plt.title("Price vs Availability")
plt.show()

# 7. Use the method to calculate the average price by neighborhood and room type
average_price = df.groupby(["neighbourhood", "room_type"]).mean()["price"]
print(average_price)

# 8. Create a heatmap to visualize the availability of listings by neighborhood
availability_pivot = df.pivot_table(
    index="neighbourhood", columns="room_type", values="availability_365"
)
sns.heatmap(availability_pivot)
plt.title("Availability Heatmap by Neighbourhood and Room Type")
plt.show()

# 9. Identify the top 10 hosts with the most listings and create a bar chart to visualize the results
top_hosts = df["host_id"].value_counts().head(10)
top_hosts.plot(kind="bar")
plt.xlabel("Host ID")
plt.ylabel("Number of Listings")
plt.title("Top 10 Hosts by Listings")
plt.show()

# 10. Analyze the relationship between the number of reviews and price by creating a scatter plot
plt.scatter(df["price"], df["number_of_reviews"], alpha=0.1)
plt.xlabel("Price")
plt.ylabel("Number of Reviews")
plt.title("Price vs Number of Reviews")
plt.show()
