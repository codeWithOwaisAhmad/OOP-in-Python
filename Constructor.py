# Python Constructors Explained for Beginners

# A constructor is a special method in Python used to initialize objects.
# The constructor method is called __init__ and runs automatically when an object is created.

# Example 1: Basic Constructor Usage
print("Basic Constructor Usage:")

class Person:
    def __init__(self, name, age):  # Constructor method
        self.name = name  # Attribute
        self.age = age    # Attribute
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object of the Person class
person1 = Person("Alice", 25)
person1.display_info()  # Output: Name: Alice, Age: 25

# Example 2: Default Constructor (Without Parameters)
print("\nDefault Constructor:")

class Greeting:
    def __init__(self):  # Constructor without parameters
        print("Hello! Welcome to Python Constructors.")

# Creating an object of the Greeting class
greet = Greeting()  # Output: Hello! Welcome to Python Constructors.

# Example 3: Constructor with Default Values
print("\nConstructor with Default Values:")

class Car:
    def __init__(self, brand="Toyota", model="Corolla"):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Creating objects with and without passing arguments
car1 = Car()  # Uses default values
car2 = Car("Honda", "Civic")

car1.display_info()  # Output: Car: Toyota Corolla
car2.display_info()  # Output: Car: Honda Civic

# Example 4: Parameterized Constructor
print("\nParameterized Constructor:")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def display_info(self):
        print(f"Student: {self.name}, Grade: {self.grade}")

# Creating an object of Student class
student1 = Student("John", "A")
student1.display_info()  # Output: Student: John, Grade: A

# The constructor (__init__) is a key part of Object-Oriented Programming in Python.
# It ensures objects are initialized with the required attributes when they are created.
