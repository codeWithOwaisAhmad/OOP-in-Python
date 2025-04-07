# Python Polymorphism Explained for Beginners

# Polymorphism is an Object-Oriented Programming (OOP) concept that means "many forms".
# It allows the same method or function to behave differently based on the object or data it is acting on.

# There are two main types of polymorphism in Python:
# 1. Compile-time Polymorphism (also known as method overloading — not directly supported in Python)
# 2. Runtime Polymorphism (achieved using method overriding and duck typing)

# Example 1: Polymorphism with Functions and Objects (Duck Typing)
print("Polymorphism with Functions and Objects:")

class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

class Cow:
    def sound(self):
        return "Moo"

# Function that takes any object with a 'sound' method
def make_sound(animal):
    print(animal.sound())

# Using different objects with the same method name
make_sound(Dog())  # Output: Bark
make_sound(Cat())  # Output: Meow
make_sound(Cow())  # Output: Moo

# This is called Duck Typing: "If it walks like a duck and quacks like a duck, it's a duck."

# Example 2: Polymorphism with Inheritance and Method Overriding
print("\nPolymorphism with Inheritance:")

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Using polymorphism
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print("Area:", shape.area())
    # Output: Area: 78.5 (for Circle), Area: 24 (for Rectangle)

# Example 3: Built-in Polymorphism
print("\nPolymorphism with Built-in Functions:")

print(len("Python"))       # Output: 6 (length of string)
print(len([1, 2, 3, 4]))    # Output: 4 (length of list)
print(len({10, 20, 30}))   # Output: 3 (length of set)

# Summary:
# - Polymorphism lets the same method work differently for different classes.
# - It's achieved using method overriding and duck typing.
# - Python uses dynamic typing to naturally support polymorphism.
# - Helps in writing more general and reusable code.
