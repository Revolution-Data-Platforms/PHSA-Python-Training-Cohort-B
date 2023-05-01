# Exercise 1
def add_numbers(num1, num2):
    return num1 + num2

print(add_numbers(2, 3))  # Output: 5


# Exercise 2
def reverse_string(string):
    return string[::-1]

print(reverse_string("hello"))  # Output: olleh


# Exercise 3
def find_largest(numbers):
    return max(numbers)

print(find_largest([3, 5, 1, 2, 8]))  # Output: 8


# Exercise 4
def find_longest(strings):
    return max(strings, key=len)

print(find_longest(["apple", "banana", "cherry", "orange"]))  # Output: banana


# Exercise 5
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello world"))  # Output: 3


# Exercise 6
def square_numbers(numbers):
    return [num ** 2 for num in numbers]

print(square_numbers([1, 2, 3, 4, 5]))  # Output: [1, 4, 9, 16, 25]


# Exercise 7
def capitalize_strings(strings):
    return [string.capitalize() for string in strings]

print(capitalize_strings(["hello", "world", "python"]))  # Output: ["Hello", "World", "Python"]


# Exercise 8
def find_average(numbers):
    return sum(numbers) / len(numbers)

print(find_average([1, 2, 3, 4, 5]))  # Output: 3.0


# Exercise 9
def is_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    return sorted(string1) == sorted(string2)

print(is_anagram("listen", "silent"))  # Output: True


# Exercise 10
def find_median(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        middle = len(numbers) // 2
        return (numbers[middle - 1] + numbers[middle]) / 2
    else:
        return numbers[len(numbers) // 2]

print(find_median([1, 2, 3, 4, 5]))  # Output: 3


# Exercise 11
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]


# Exercise 12
strings = ["hello", "world", "python"]
uppercase_strings = list(map(lambda x: x.upper(), strings))
print(uppercase_strings)  # Output: ['HELLO', 'WORLD', 'PYTHON']


# Exercise 13
def average_args(*args):
    return sum(args) / len(args)

print(average_args(1, 2, 3, 4, 5))  # Output: 3.0


# Exercise 14
def reverse_kwargs(**kwargs):
    return {value: key for key, value in kwargs.items()}

print(reverse_kwargs(name="Alice", age=30, location="London"))  # Output: {'Alice': 'name', 30: 'age', 'London': 'location'}


# Exercise 15
def calculate_student_average(student):
    total = sum(student["grades"])
    count = len(student["grades"])
    average = total / count
    return average

def find_top_student(students):
    top_student = max(students, key=lambda student: student["average"])
    return top_student

def find_bottom_student(students):
    bottom_student = min(students, key=lambda student: student["average"])
    return bottom_student

def calculate_class_average(students):
    total_class_average = sum(student["average"] for student in students)
    class_average = total_class_average / len(students)
    return class_average

students = [
    {"name": "Alice", "grades": [90, 85, 88]},
    {"name": "Bob", "grades": [80, 75, 78]},
    {"name": "Charlie", "grades": [87, 91, 94]},
    {"name": "David", "grades": [76, 82, 85]},
    {"name": "Eve", "grades": [90, 92, 95]}
]

# Calculate the average grade for each student
for student in students:
    student["average"] = calculate_student_average(student)

# Find the top student
top_student = find_top_student(students)
print(f"The top student is {top_student['name']} with an average grade of {top_student['average']:.2f}")

# Find the bottom student
bottom_student = find_bottom_student(students)
print(f"The bottom student is {bottom_student['name']} with an average grade of {bottom_student['average']:.2f}")

# Calculate the overall class average
class_average = calculate_class_average(students)
print(f"The class average is {class_average:.2f}")
