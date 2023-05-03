import pandas as pd
import numpy as np

# Generating random data for the first DataFrame
np.random.seed(123)
df1 = pd.DataFrame(
    {
        "ID": np.arange(1000),
        "Age": np.random.randint(18, 65, 1000),
        "Country": np.random.choice(["USA", "Canada", "France", "UK"], 1000),
    }
)

# Exercise 1
print(df1.head(10))

# Exercise 2
print(df1.shape)

# Exercise 3
print(df1["Age"])

# Exercise 4
print(df1[["ID", "Country"]])

# Exercise 5
filtered_df = df1[df1["Age"] <= 60]
print(filtered_df)

# Exercise 6
np.random.seed(456)
df2 = pd.DataFrame(
    {
        "ID": np.arange(1000),
        "Salary": np.random.randint(50000, 100000, 1000),
        "Department": np.random.choice(
            ["Sales", "Marketing", "Engineering", "Finance"], 1000
        ),
    }
)
merged_df = pd.merge(df1, df2, on="ID")

# Exercise 7
merged_df["Bonus"] = merged_df["Salary"] * 0.1

# Exercise 8
sorted_df = merged_df.sort_values(
    ["Department", "Salary"], ascending=[True, False]
)
print(sorted_df)

# Exercise 9
grouped_df = merged_df.groupby("Department")["Salary"].agg(
    ["mean", "median", "std"]
)
print(grouped_df)

# Exercise 10
merged_df.loc[merged_df["Department"] == "Sales", "Salary"] *= 1.1

# Exercise 10
merged_df.loc[
    (merged_df["Country"] == "Canada")
    & (merged_df["Department"] == "Engineering"),
    "Salary",
] = 100000
print(merged_df)


# Exercise 12
def salary_range(salary):
    if salary < 60000:
        return "low"
    elif salary < 80000:
        return "medium"
    else:
        return "high"


merged_df["salary_range"] = merged_df["Salary"].apply(salary_range)

# Exercise 13
pivot_table = pd.pivot_table(
    merged_df,
    values="Salary",
    index=["Department"],
    columns=["Age"],
    aggfunc=np.mean,
)
print(pivot_table)
