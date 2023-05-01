import matplotlib.pyplot as plt

# Exercise 1
x = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
y = [
    10000,
    15000,
    12000,
    18000,
    20000,
    25000,
    30000,
    28000,
    32000,
    35000,
    38000,
    40000,
]
plt.plot(x, y)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Trend")
plt.show()

# Exercise 2
height = [60, 65, 68, 70, 72, 74, 75, 77, 79, 80]
weight = [100, 120, 140, 160, 180, 190, 200, 210, 220, 230]
plt.scatter(weight, height)
plt.xlabel("Weight")
plt.ylabel("Height")
plt.title("Weight vs. Height")
plt.show()

# Exercise 3
countries = ["USA", "China", "Japan", "Australia", "Russia"]
medals = [113, 88, 58, 46, 71]
plt.bar(countries, medals)
plt.xlabel("Country")
plt.ylabel("Medals")
plt.title("2020 Olympics Medal Count")
plt.show()

# Exercise 4
fruits = ["Apples", "Oranges", "Bananas", "Grapes", "Mangos"]
percentages = [30, 25, 20, 15, 10]
plt.pie(percentages, labels=fruits)
plt.title("Fruit Basket")
plt.show()

# Exercise 5
grades = [
    85,
    92,
    80,
    75,
    95,
    88,
    89,
    93,
    90,
    84,
    87,
    91,
    89,
    83,
    85,
    92,
    94,
    88,
    85,
    86,
]
plt.hist(grades, bins=5)
plt.xlabel("Grade")
plt.ylabel("Frequency")
plt.title("Grade Distribution")
plt.show()

# Exercise 6
heights = [68, 72, 70, 75, 74, 71, 73, 69, 76, 72, 74, 77, 75, 72, 73, 70]
plt.boxplot(heights)
plt.ylabel("Height")
plt.title("Basketball Player Height Distribution")
plt.show()

# Exercise 7
temperatures = [10, 15, 11, 18, 20, 22, 25]
dates = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
plt.plot(dates, temperatures)
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trend")
plt.show()

# Exercise 8
prices = [20, 30, 25, 40, 50, 35, 45, 60, 55, 70]
quality = [3, 2, 4, 2, 1, 4, 3, 1, 2, 1]
plt.scatter(prices, quality)
plt.xlabel("Price ($)")
plt.ylabel("Quality (1-5)")
plt.title("Price vs. Quality")
plt.show()

# Exercise 9
categories = [
    "Housing",
    "Transportation",
    "Food",
    "Utilities",
    "Entertainment",
]
expenses1 = [20, 10, 30, 15, 25]
expenses2 = [25, 20, 15, 20, 20]
expenses3 = [10, 30, 20, 15, 25]
x = range(len(categories))
plt.bar(x, expenses1, label="January", bottom=expenses2, color="red")
plt.bar(x, expenses2, label="February", bottom=expenses3, color="blue")
plt.bar(x, expenses3, label="March", color="green")
plt.xticks(x, categories)
plt.xlabel("Category")
plt.ylabel("Percentage")
plt.title("Budget Expenses")
plt.legend()
plt.show()

# Exercise 10
areas = [
    "Communication",
    "Teamwork",
    "Leadership",
    "Problem-solving",
    "Creativity",
]
team1_scores = [4, 3, 5, 3, 4]
team2_scores = [3, 4, 4, 5, 3]
team3_scores = [5, 5, 3, 4, 5]
team4_scores = [4, 4, 4, 4, 4]
angles = [n / float(len(areas)) * 2 * 3.14 for n in range(len(areas))]
angles += angles[:1]
plt.polar(angles, team1_scores + [team1_scores[0]], label="Team 1")
plt.polar(angles, team2_scores + [team2_scores[0]], label="Team 2")
plt.polar(angles, team3_scores + [team3_scores[0]], label="Team 3")
plt.polar(angles, team4_scores + [team4_scores[0]], label="Team 4")
plt.xticks(angles[:-1], areas)
plt.title("Team Performance")
plt.legend()
plt.show()
