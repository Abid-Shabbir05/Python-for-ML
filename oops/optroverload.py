# What is operator overloading in oops exactly


# Special (dunder/magic) methods = control the behavior of objects

# These methods tell Python how your objects should act in different situations.

# They control the behavior of objects for:

# Creation → __init__

# Printing → __str__

# Operators → __add__, __sub__, __mul__, etc.

# Comparisons → __eq__, __lt__, __gt__, etc.

# Other built-in actions → __len__, __getitem__, etc.

#  In simple words

# Special methods are like rules you set for your object, so Python knows how your object should behave when you use it in operations or functions.


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __add__(self, other):   # Overloading +
#         return Vector(self.x + other.x, self.y + other.y)
    
#     def __str__(self):          # For printing
#         return f"({self.x}, {self.y})"

# # Create objects
# v1 = Vector(2, 3)
# v2 = Vector(4, 5)

# # Use + operator
# v3 = v1 + v2
# print(v3)



class Overloading:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Overloading(self.a + other.a, self.b + other.b)
    
    def __str__(self):
        return f"({self.a}, {self.b})"

o1 = Overloading(10, 20)
o2 = Overloading(5, 10)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)

print(p1 + p2)   # (6, 8)
print(p2 - p1)   # (2, 2)
print(p1 == p2)  # False
