# Exercise 1: Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Exercise 2: Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

# Exercise 3: Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Exercise 4: Student class
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def study(self):
        print(f"I am studying {self.major}.")

# Exercise 5: Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_age(self):
        current_year = 2023
        return current_year - self.year

# Exercise 6: Employee class
class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def total_pay(self):
        return self.salary + self.bonus

# Exercise 7: BankAccount class
class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def add_interest(self):
        self.balance *= 1 + self.interest_rate

# Exercise 8: ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def total_cost(self):
        return sum(item.price for item in self.items)

# Exercise 9: Employee subclass
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def work(self):
        print(f"I am working and earning {self.salary} dollars per hour.")


# Exercise 10: BankAccount subclasses
class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def add_interest(self):
        self.balance *= 1 + self.interest_rate

class CheckingAccount(BankAccount):
    def __init__(self, balance, interest_rate, overdraft_fee):
        super().__init__(balance, interest_rate)
        self.overdraft_fee = overdraft_fee

    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= self.overdraft_fee
        self.balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate, minimum_balance):
        super().__init__(balance, interest_rate)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("Cannot withdraw below minimum balance.")
        else:
            self.balance -= amount
