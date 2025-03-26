# Python Objects Explained for Beginners

# Objects are instances of a class. They hold data (attributes) and behaviors (methods).
# Everything in Python is an object, including integers, strings, lists, and user-defined classes.

# Example 1: Creating a Class and an Object
print("Creating an Object from a Class:")

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Attribute
        self.model = model  # Attribute
        self.year = year    # Attribute
    
    def display_info(self):
        print(f"Car: {self.brand} {self.model} ({self.year})")

# Creating an object of the Car class
car1 = Car("Toyota", "Corolla", 2022)
car1.display_info()  # Output: Car: Toyota Corolla (2022)

# Example 2: Multiple Objects
print("\nCreating Multiple Objects:")
car2 = Car("Honda", "Civic", 2023)
car3 = Car("Ford", "Mustang", 2021)

car2.display_info()  # Output: Car: Honda Civic (2023)
car3.display_info()  # Output: Car: Ford Mustang (2021)

# Example 3: Modifying Object Attributes
print("\nModifying Object Attributes:")
car1.year = 2025  # Changing the year attribute
car1.display_info()  # Output: Car: Toyota Corolla (2025)

# Example 4: Deleting an Object Attribute
print("\nDeleting an Object Attribute:")
del car1.year  # Deleting the year attribute
# print(car1.year)  # This will raise an AttributeError since 'year' is deleted

# Example 5: Checking Object Type
print("\nChecking Object Type:")
print(isinstance(car1, Car))  # Output: True (car1 is an instance of Car)
print(isinstance(42, Car))    # Output: False (42 is not an instance of Car)

# Objects are fundamental in Python and are used to structure code efficiently!
# They allow real-world problem representation and are the foundation of Object-Oriented Programming (OOP).
