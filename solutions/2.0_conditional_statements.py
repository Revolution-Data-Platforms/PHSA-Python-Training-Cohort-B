# Exercise 1
temperature = float(input("Enter the temperature: "))

if temperature > 90:
    print("too hot")
elif temperature < 60:
    print("too cold")
else:
    print("just right")

# Exercise 2
number = int(input("Enter a number: "))

if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

# Exercise 3
character = input("Enter a character: ")

if character.isupper():
    print("uppercase")
elif character.islower():
    print("lowercase")
else:
    print("not a letter")

# Exercise 4
year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("leap year")
else:
    print("not a leap year")

# Exercise 5
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if number1 > 0 and number2 > 0:
    print("both positive")
elif number1 < 0 and number2 < 0:
    print("both negative")
else:
    print("mixed")

# Exercise 6
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("even")
else:
    print("odd")

# Exercise 7
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("multiple of both 3 and 5")
elif number % 3 == 0:
    print("multiple of 3")
elif number % 5 == 0:
    print("multiple of 5")
else:
    print("not a multiple of 3 or 5")

# Exercise 8
string = input("Enter a string: ")

if string == string[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

# Exercise 9
grade = int(input("Enter the grade: "))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

# Exercise 10
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if sorted(string1) == sorted(string2):
    print("anagram")
else:
    print("not anagram")
