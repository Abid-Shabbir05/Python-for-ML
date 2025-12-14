# OOPs (object oriented programing language) 
# oops is a way to write clean, logical and real world like program by organizing code using class and object
# so we use oops  to organize and manage complex program easily because in OOps we are coding around a
# object instead of loose function and steps 
# advantages of oops :
# provide a clear struture to program
# make code easier to maintain ,reuse, debug
# modularity
# scalability

#  ====== programs ====
# Class 
# class is a blue print or templeate for the object that define attribute(variable) object should have
# and what methode(function ) object can perform

# class MyClass:
#     x = 5
# p1 = MyClass() # P1 is the object
# print(p1.x)




#  def __init__() methode (constructor)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

P1 = Person("Abid", 23)
print(P1.name)
print(P1.age)
        
# The __str__() method is a s} is {self.gpa}"
#  pecial method in Python.
# It defines what should be printed when you print an object.
# class Student:
#     def __init__(self, name, mark):
#         self.name = name
#         self.mark = mark
        
#     def __str__(self):
#         return f"{self.name} {self.mark}"

# S1 = Student("Ali", 90)
# print(S1)

class Student1:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    def welcome(self):
        print(f"Wellcome {self.name} to our colledge")
    
    def get_mark(self):
        return self.gpa

S2 = Student1("Sara", 3)
S2.welcome()
print(S2.get_mark())

# Example:
class Student2:
    def __init__(self, name, marks):
        self.name = name 
        self.mark = marks

    def get_avg(self):
        sum = 0
        for val in self.mark:
            sum += val
        print(f"HI {self.name} your mark is {sum/3}")


S3 = Student2("Abid", [80, 70, 99])
S3.get_avg()

# A decorator is a special function or keyword that adds extra behavior to a function or method
#  without changing its code directly. It's usually placed above a function or method with an @ symbol.
# @staticmethod is a decorator used inside a class to define a method that doesn’t need access to self or cls.
# The method belongs to the class, not to any object.

class Calculator:
    @staticmethod   # decorator
    def add(x, y):
        return x+y
print(Calculator.add(5, 4))


