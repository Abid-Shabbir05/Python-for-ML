# 1- here we will learn about variable and datatype in python.
# 2- in python there is no spacefic keyword to initialize the datat type 
# so we initiaze data by any name as belove.
# 3- to display output use print()command in python
# 4- we also discuss the key-words in python 
# key-words are reserved words in python each have a spacific function in prgroming
# key-words can not be set as identifier

name = "Abid"   
age = 22
gpa = 3.9

print(f"name: {name} ,age :{age} ,gpa: {gpa}" )

# the type() function use to check the type of value store in a variable
print(type(name))
print(type(age))
print(type(gpa))

# in python generally we learn about five type of variable
# strings
# integers
# boolean
# float
# None

age1 = 24
old = False
a = None
yng = True
print(type(age1))
print(type(old))
print(type(a))
print(type(yng))



num1 = 1200
num2 = 1500
sum = num1 + num2
print(f"sum of two number is: {sum} ")