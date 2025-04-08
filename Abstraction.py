# Python Abstraction Explained for Beginners

# Abstraction is one of the four fundamental concepts in Object-Oriented Programming (OOP).
# It means hiding complex implementation details and showing only the essential features of an object.
# In Python, abstraction is achieved using abstract classes and abstract methods.

# To use abstraction, Python provides the `abc` module (Abstract Base Classes).
# We use the `ABC` class and the `@abstractmethod` decorator from the `abc` module.

from abc import ABC, abstractmethod

# Example 1: Basic Abstraction with Abstract Class
print("Abstraction Example with Abstract Class:")

class Vehicle(ABC):
    # Abstract method
    @abstractmethod
    def start_engine(self):
        pass

    # Regular method
    def stop_engine(self):
        print("Engine stopped.")

# Now we create subclasses that implement the abstract method
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with a key.")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with a button.")

# Creating objects of the concrete classes
car = Car()
bike = Bike()

car.start_engine()       # Output: Car engine started with a key.
car.stop_engine()        # Output: Engine stopped.

bike.start_engine()      # Output: Bike engine started with a button.
bike.stop_engine()       # Output: Engine stopped.

# If we try to create an object of the abstract class directly, Python will raise an error:
# v = Vehicle()  -> This will throw TypeError: Can't instantiate abstract class Vehicle with abstract method start_engine

# Why use Abstraction?
# - It helps in reducing code complexity.
# - Makes code more secure by hiding unnecessary implementation details.
# - Allows you to define a common interface for different types of objects.

# Summary:
# - Abstract classes cannot be instantiated directly.
# - Any class with at least one abstract method is abstract.
# - Abstract methods are declared using the @abstractmethod decorator.
# - Subclasses must override all abstract methods.
# - Promotes cleaner, modular, and more understandable code.

# Abstraction is like using a TV remote — you press buttons without knowing the internal mechanism!
