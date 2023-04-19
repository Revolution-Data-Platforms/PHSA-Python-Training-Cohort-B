# Exercise 1
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)

# Exercise 2
my_dict["job"] = "programmer"
print(my_dict)

# Exercise 3
my_dict["age"] = 35
print(my_dict)

# Exercise 4
squares_dict = {i: i**2 for i in range(1, 6)}
print(squares_dict)

# Exercise 5
sum(dictionary.values())

# Example usage
my_dict = {"a": 1, "b": 2, "c": 3}
sum_values = sum(my_dict.values())
print(sum_values)  # Output: 6

# Exercise 6
{**dict1, **dict2}

# Example usage
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {"a": 1, "b": 2, "c": 3, "d": 4}

# Exercise 7
word_counts = {}
with open("filename.txt") as f:
    for line in f:
        words = line.strip().split()
        for word in words:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
print(word_counts)

# Exercise 8
user_info = {}
user_info["name"] = input("What is your name? ")
user_info["age"] = input("How old are you? ")
user_info["favorite_color"] = input("What is your favorite color? ")
print(user_info)

# Exercise 9
fruit_prices = {"apple": 0.5, "banana": 0.25, "orange": 0.75}
fruit_name = input("Enter a fruit name: ")
if fruit_name in fruit_prices:
    print(fruit_prices[fruit_name])
else:
    print("Fruit not found.")

# Exercise 10
student_scores = {"John": [80, 85, 90], "Jane": [90, 95, 100], "Bob": [70, 75, 80]}
student_name = input("Enter a student name: ")
if student_name in student_scores:
    avg_score = sum(student_scores[student_name]) / len(student_scores[student_name])
    print(avg_score)
else:
    print("Student not found.")
