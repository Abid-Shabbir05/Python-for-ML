# The sys module in Python is a built-in module that provides access to some variables 
# and functions used or maintained by the Python interpreter. Essentially, it allows your
# Python program to interact with the interpreter itself.



# sys.argv in Python
# sys.argv is a list in Python, which contains the command-line arguments passed to a Python script.
# It comes from the sys module, so you need to import it first.
import sys
# name = sys.argv[1]
# print(f"Hellow Mr {name}")

print(sys.path)

# What is sys.path?
# Python needs to find modules when you do import something.
# sys.path is just a list of folders where Python looks for modules.
# If your module is in one of these folders, Python can import it. If not, it fails.

import os
sys.path

print(sys.platform)# retrun current operating system
print(sys.version) #Returns a detailed string about the Python version you’re running.

# sys.exit is a function in Python’s sys module that is used to terminate the program 
# (exit from Python interpreter or script execution).

import sys

print("Before exit")
sys.exit(0)   # Exit successfully
print("This will never print")


# sys.getsizeof(object) → Returns the size of an object in bytes (how much memory it takes in RAM).
s = [1,2,3,4,5]
print(sys.getsizeof(s))

import sys
print(sys.getrecursionlimit())   # usually 1000
# sys.setrecursionlimit() is only useful for recursive functions (where the function calls itself).
# In your iterative version, there’s no recursion, so Python never hits the recursion depth limit → 
# you don’t need sys.setrecursionlimit() at all.