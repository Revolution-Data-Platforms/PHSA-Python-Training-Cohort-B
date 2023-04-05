# Exercise 1
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

# Access the second fruit in the list.
print(fruits[1]) # Output: banana

# Access the last fruit in the list using negative indexing.
print(fruits[-1]) # Output: kiwi

# Access the first three fruits in the list using slicing.
print(fruits[:3]) # Output: ["apple", "banana", "cherry"]

# d. Change the value of the last fruit in the list to "grape".
fruits[-1] = "grape"
print(fruits) # ['apple', 'banana', 'cherry', 'orange', 'grape']

# Exercise 2
word = "hello, world"

# Access the first character in the string.
print(word[0]) # Output: h

# Access the last character in the string using negative indexing.
print(word[-1]) # Output: .

# Access the sub-string "hello" in the string.
print(word[:5]) # Output: hello


# Exercise 3
numbers = (1, 2, 3, 4, 5)

# Access the first number in the tuple.
print(numbers[0]) # Output: 1

# Access the last number in the tuple using negative indexing.
print(numbers[-1]) # Output: 5

# Access the first three numbers in the tuple using slicing.
print(numbers[:3]) # Output: (1, 2, 3)


# Exercise 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Access every other number in the list using slicing.
print(numbers[::2]) # Output: [1, 3, 5, 7, 9]

# Access the last five numbers in the list using slicing.
print(numbers[-5:]) # Output: [6, 7, 8, 9, 10]

# Access the numbers from the middle of the list to the end using slicing.
print(numbers[5:]) # Output: [6, 7, 8, 9, 10]

# Change the value of every even number in the list to the string "even".
numbers[1::2] = ["even"] * 5
print(numbers) # Output: [1, 'even', 3, 'even', 5, 'even', 7, 'even', 9, 'even']


# Exercise 5
sentence = "The quick brown fox jumps over the lazy dog."

# Access the first 10 characters in the string.
print(sentence[:10]) # Output: The quick

# Access the last 10 characters in the string using negative indexing.
print(sentence[-10:]) # Output: the lazy dog.

# Access the sub-string "quick brown" in the string.
print(sentence[4:15]) # Output: quick brown
