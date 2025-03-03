# List in Python
# A list in Python is an ordered, mutable (changeable) collection that can hold multiple 
# items of different data types (integers, strings, floats, etc.).
# Key Features of Lists
# ✔ Ordered – Elements maintain their order
# ✔ Mutable – Can be modified (add, remove, change elements)
# ✔ Allows Duplicates – Can contain the same value multiple times
# ✔ Supports Different Data Types – Can store integers, strings, floats, etc.
# A list is a built-in data type in Python but is also considered a data structure because 
# it helps organize and store multiple elements efficiently.

mark = [90,78,97,45,67,90]
print(mark)
print(len(mark))
print(type(mark))
print(mark[0]) # it display the first element at index 0
print(mark[1]) 

student = ["Abid","Arif","kumail","jameel"]
student[0] = "Abidshabbir" # i can change any element b/c list is mutalbe
print(student)

#dynamic list
dynamic = [18,"Abid",3.14,True,]
print(dynamic)

#List Slicing in Python
# Slicing allows you to access a subset of elements from a list using the following
# list[start:end:step]
# start → Index where the slice begins (default: 0)
# end → Index where the slice stops (not included in the result)
# step → Defines the gap between elements (default: 1)

mark = [90, 78, 97, 45, 67, 90, 60, 70, 80]
print(mark[0:7:2])# it will print every 2nd items in the list
print(mark[0:])
print(mark[0:5])
print(mark[0:])
print(mark[::-1])
print(mark[::-1]) # it will print list itms reversly



