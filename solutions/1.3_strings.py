# Exercise 1: Write a program that takes a name as input and greets the user using their name.
name = input("Enter your name: ")
print("Hello", name + "!")

# Exercise 2: Write a program that takes the string "Hello there!" and prints the string in all uppercase letters.
string = "Hello there!"
print(string.upper())

# Exercise 3: Write a program that splits the string "Let's split into groups." into words and prints the result.
string = "Let's split into groups."
words = string.split()
print(words)

# Exercise 4: Write a program that takes the string "I love blank!" and replaces the word blank with Python.
string = "I love blank!"
new_string = string.replace("blank", "Python")
print(new_string)

# Exercise 5: Write a program that reverses the string "Did Hannah see bees? Hannah did."
string = "Did Hannah see bees? Hannah did."
reversed_string = string[::-1]
print(reversed_string)
