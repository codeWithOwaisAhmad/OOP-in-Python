# Python Classes Explained for Beginners (Detailed Version)

# What are Classes in Python?
# A class is a blueprint for creating objects. It defines attributes (variables) and methods (functions) that an object can have.
# Classes allow us to implement Object-Oriented Programming (OOP) principles like Encapsulation, Inheritance, and Polymorphism.

# Defining a Class:
print("\nDefining and Using a Class:")
class Person:
    def __init__(self, name, age):  # Constructor Method
        self.name = name  # Instance Variable
        self.age = age
    
    def introduce(self):  # Method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an Object (Instance of a Class)
p1 = Person("Alice", 25)
p1.introduce()
# Output:
# Hello, my name is Alice and I am 25 years old.

# Example 2: Class with Default Values
print("\nClass with Default Values:")
class Car:
    def __init__(self, brand="Toyota", model="Corolla"):
        self.brand = brand
        self.model = model
    
    def show_car(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

car1 = Car()  # Using default values
car1.show_car()
car2 = Car("Honda", "Civic")  # Custom values
car2.show_car()
# Output:
# Car Brand: Toyota, Model: Corolla
# Car Brand: Honda, Model: Civic

# Example 3: Class with Inheritance
print("\nClass Inheritance:")
class Animal:
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        print("Some generic animal sound")

# Inheriting from Animal class
class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")  # Calling Parent Class Constructor
        self.name = name
    
    def make_sound(self):
        print("Woof! Woof!")

my_dog = Dog("Buddy")
print(f"My pet is a {my_dog.species} named {my_dog.name}.")
my_dog.make_sound()
# Output:
# My pet is a Dog named Buddy.
# Woof! Woof!

# Example 4: Private and Public Variables
print("\nPrivate and Public Variables:")
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Public Variable
        self.__balance = balance  # Private Variable (Encapsulation)
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
        else:
            print("Insufficient funds!")
    
    def get_balance(self):  # Public Method to Access Private Variable
        return self.__balance

account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(300)
print("Balance:", account.get_balance())
# Output:
# Deposited 500. New balance: 1500
# Withdrew 300. Remaining balance: 1200
# Balance: 1200

# Important Concepts of Classes:
# 1. **Encapsulation** - Restricting access to certain details (using private variables and methods).
# 2. **Inheritance** - Creating a new class from an existing class to reuse code.
# 3. **Polymorphism** - Methods in different classes sharing the same name but having different behaviors.
# 4. **Abstraction** - Hiding complex implementation details and exposing only necessary parts.

# Classes make code more structured, reusable, and maintainable!
