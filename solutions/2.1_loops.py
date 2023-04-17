# Exercise 1
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print(sum)

# Exercise 2
number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Exercise 3
limit = 50
a, b = 0, 1
while b < limit:
    print(b, end=" ")
    a, b = b, a + b

# Exercise 4
numbers = [1, 5, 2, 8, 3]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)

# Exercise 5
number = 17
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
if is_prime:
    print("Prime")
else:
    print("Not Prime")

# Exercise 6
string = "Hello World"
i = 0
while i < len(string):
    if string[i] == ' ':
        i += 1
        continue
    print(string[i])
    i += 1

# Exercise 7
n = 10
count = 0
i = 2
while count < n:
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")
        count += 1
    i += 1

# Exercise 8
words = ['apple', 'banana', 'cherry', 'apple']
target_word = 'apple'
for index, word in enumerate(words):
    if word == target_word:
        print(index)
        break


# Exercise 9
numbers = [1, 5, 2, 8, 3]
smallest = numbers[0]
second_smallest = None
for number in numbers:
    if number < smallest:
        second_smallest = smallest
        smallest = number
    elif number != smallest and (second_smallest is None or number < second_smallest):
        second_smallest = number
print(second_smallest)

# Exercise 10
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()  # Adding an empty line to separate each multiplication set
