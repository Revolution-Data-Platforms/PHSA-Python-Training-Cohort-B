# Exercise 1
favorite_foods = ['pizza', 'sushi', 'tacos', 'ice cream', 'burger']

# Exercise 2
print(len(favorite_foods))

# Exercise 3
print(favorite_foods[-2])

# Exercise 4
favorite_foods.sort(reverse=True)
print(favorite_foods)

# Exercise 5
favorite_foods[0] = 'pasta'
print(favorite_foods)

# Exercise 6
favorite_foods.append('ramen')
print(favorite_foods)

# Exercise 7
favorite_foods.remove('sushi')
print(favorite_foods)
## Alternative Solution
del favorite_foods[1]
print(favorite_foods)

# Exercise 8
people = [['John', 30, 'pizza'], ['Jane', 35, 'sushi'], ['Jim', 40, 'tacos']]

# Exercise 9
new_person = ['Jake', 25, 'ramen']
people.append(new_person)
print(people)

# Exercise 10
for person in people:
    print(person[0])

# Exercise 11
total_age = 0
for person in people:
    total_age += person[1]
average_age = total_age / len(people)
print(average_age)

# Exercise 12
people_favorite_foods = ''
for person in people:
    people_favorite_foods += person[2] + ' '
print(people_favorite_foods)

# Exercise 13
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of_evens = [x**2 for x in numbers if x % 2 == 0]
print(squares_of_evens)

# Exercise 14
string = "The Quick Brown Fox Jumps Over The Lazy Dog"
uppercase_letters = [char for char in string if char.isupper()]
print(uppercase_letters)

# Exercise 15
sentence = "The quick brown fox jumps over the lazy dog"
word_lengths = [len(word) for word in sentence.split()]
print(word_lengths)
