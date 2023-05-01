import requests
import matplotlib.pyplot as plt

# Import the data from the API
url = "https://api.covid19api.com/dayone/country/canada"
response = requests.get(url)
data = response.json()

# Create a line chart showing the total number of confirmed cases in Canada
# over time.
confirmed_cases = [day["Confirmed"] for day in data]
# Extract the date from each day.
dates = [day["Date"][:10] for day in data]
# Make every 2nd month a tick label.
date_ticks = [date for date in dates if date[8:] == "01"][::2]

plt.plot(dates, confirmed_cases)
plt.title("Total Confirmed Cases in Canada")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.xticks(date_ticks, rotation=45)
plt.show()

# Create a bar chart showing the total number of confirmed cases and deaths in
# Canada.
confirmed_cases = [day["Confirmed"] for day in data]
deaths = [day["Deaths"] for day in data]

total_confirmed = confirmed_cases[-1]
total_deaths = deaths[-1]

data = [total_confirmed, total_deaths]

x = ["Confirmed", "Deaths"]

plt.bar(x, data, color=["blue", "red"], log=True)

plt.title("Total Cases in Canada")
plt.ylabel("Number of Cases")
plt.xticks(rotation=45)

plt.show()


# Create a pie chart showing the percentage of confirmed cases and deaths in
# Canada.
labels = ["Confirmed", "Deaths"]
sizes = [total_confirmed, total_deaths]
colors = ["skyblue", "lightcoral"]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, shadow=True)
plt.legend(title="Legend", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Total Cases in Canada")
plt.show()

# Save the graphs as images.
plt.savefig("confirmed_cases.png")
plt.savefig("total_cases.png")
plt.savefig("pie_chart.png")
