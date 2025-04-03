# Python Inheritance Explained for Beginners

# Inheritance is an Object-Oriented Programming (OOP) concept that allows a class to derive properties and behaviors from another class.
# It promotes code reusability and hierarchy in programming.

# Example 1: Single Inheritance
print("Single Inheritance Example:")

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some generic sound"

class Dog(Animal):  # Dog class inherits from Animal class
    def speak(self):
        return "Bark!"

# Creating objects
animal = Animal("Generic Animal")
dog = Dog("Buddy")

print(animal.name, "says:", animal.speak())  # Output: Generic Animal says: Some generic sound
print(dog.name, "says:", dog.speak())  # Output: Buddy says: Bark!

# Example 2: Multiple Inheritance
print("\nMultiple Inheritance Example:")

class Parent1:
    def feature1(self):
        return "Feature 1 from Parent1"

class Parent2:
    def feature2(self):
        return "Feature 2 from Parent2"

class Child(Parent1, Parent2):  # Child inherits from both Parent1 and Parent2
    def feature3(self):
        return "Feature 3 from Child"

child_obj = Child()
print(child_obj.feature1())  # Output: Feature 1 from Parent1
print(child_obj.feature2())  # Output: Feature 2 from Parent2
print(child_obj.feature3())  # Output: Feature 3 from Child

# Example 3: Multilevel Inheritance
print("\nMultilevel Inheritance Example:")

class Grandparent:
    def grand_feature(self):
        return "Grandparent's Feature"

class Parent(Grandparent):
    def parent_feature(self):
        return "Parent's Feature"

class Child(Parent):
    def child_feature(self):
        return "Child's Feature"

child_obj = Child()
print(child_obj.grand_feature())  # Output: Grandparent's Feature
print(child_obj.parent_feature())  # Output: Parent's Feature
print(child_obj.child_feature())  # Output: Child's Feature

# Example 4: Method Overriding
print("\nMethod Overriding Example:")

class Vehicle:
    def description(self):
        return "This is a vehicle"

class Car(Vehicle):
    def description(self):
        return "This is a car"

car = Car()
print(car.description())  # Output: This is a car

# Summary:
# - Inheritance allows one class to acquire the attributes and methods of another.
# - Single, multiple, and multilevel inheritance are common types.
# - Method overriding lets a child class redefine a method from the parent class.

# Inheritance simplifies code reuse and establishes relationships between classes!
