# Abstraction means showing only the essential features of an object and hiding unnecessary details.

#  It focuses on what an object does instead of how it does it.

#  Example in Real Life

# When you drive a car, you just use the steering wheel, brake, accelerator.

# You don’t care how the engine, gears, or fuel system works internally.

# This is abstraction: you interact with simple things, while complexity is hidden.
# Why Use Abstraction?

# To reduce complexity in programming.

# To focus on high-level design instead of low-level details.

# To make code more modular, reusable, and maintainable.

#  How is Abstraction Implemented in Python?

# In Python, abstraction is usually implemented using:

# Abstract Classes (from abc module)

# Abstract Methods (methods that are declared but not implemented)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def Area(self, ):
        return self.l * self.w
    
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def Area(self):
        return 3.14 * self.r * self.r
        

shaps = [Rectangle(5, 3), Circle(3)]
print(type(shaps))
for s in shaps:
    print(s.Area())