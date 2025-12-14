
# Encapsulation in Object-Oriented Programming (OOP) means binding data (attributes/variables) and the methods (functions) 
# that operate on that data together into a single unit (class), and controlling access to that data.

# In simpler words:
# It’s like putting data and the code that works on it inside a protective capsule (class), so outside code cannot
# directly mess with it.


# Key Points of Encapsulation:

# Data Hiding –
# You restrict direct access to some parts of an object. Instead of exposing everything, you give controlled access

# (via getters/setters or methods).
# Security –
# It prevents accidental or unauthorized modification of important data.

# Abstraction Support –
# Users don’t need to know how data is stored internally, they just use the provided methods.
# class BankAccount:

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self.__balance = balance    # Private attribute (hidden)

    # Public method to view balance (controlled access)
    def get_balance(self):
        return self.__balance

    # Public method to deposit safely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}, new balance = {self.__balance}"
        else:
            return "Deposit amount must be positive"

    # Public method to withdraw safely
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}, new balance = {self.__balance}"
        else:
            return "Invalid withdrawal amount"

# Using the class
acc = BankAccount("Abid", 1000)
print(acc.get_balance())     # Access balance safely
print(acc.deposit(500))      # Deposits safely
print(acc.withdraw(200))     # Withdraws safely

print(acc.__balance)         # Error: Cannot access directly (encapsulation)





