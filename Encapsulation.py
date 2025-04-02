# Python Encapsulation Explained for Beginners

# Encapsulation is an Object-Oriented Programming (OOP) concept that restricts direct access to data.
# It protects the integrity of data by allowing controlled access using methods.

# Example 1: Using Private Attributes
print("Encapsulation Using Private Attributes:")

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute (prefix with __)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount!")
    
    def get_balance(self):  # Public method to access private data
        return self.__balance

# Creating an object of BankAccount class
account = BankAccount("Alice", 1000)
account.deposit(500)  # Output: Deposited: 500. New Balance: 1500
account.withdraw(200)  # Output: Withdrew: 200. New Balance: 1300

# Trying to access the private attribute directly (will raise an error)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Correct way to access private attribute
print("Balance:", account.get_balance())  # Output: Balance: 1300

# Example 2: Using Property Decorators for Encapsulation
print("\nEncapsulation Using Property Decorators:")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Salary must be positive!")
    
# Creating an object of Employee class
emp = Employee("John", 5000)
print(emp.salary)  # Output: 5000 (Accessing private variable using property)
emp.salary = 6000  # Modifying salary using setter
print(emp.salary)  # Output: 6000

# Trying to set negative salary
emp.salary = -3000  # Output: Salary must be positive!

# Encapsulation helps in data hiding, preventing unauthorized access,
# and implementing controlled modifications through methods.
