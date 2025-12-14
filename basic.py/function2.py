# Function is a block of code which only run when it is called
# arbitrary keywords argument (**kwargs) if you don't know how many argument that will be passed in your
# function add two **asterisk before the parameter name in the function defination
# Example:

def Student(**std):
    print(f"student name is { std["std1"]} ")
Student(std1 = "Abid", std2 = "tanveer", std3 = "qoli")

def name(**child):
    print(f"child name is { child["old"] }")
name(old = "Ali", young = "Hasan", little = "baqir")


# Lamda function:
# lambda is simply an anonymous function without a name
# in python these are used to created lambda keyword thats way they are also called lambda function
# syntax
# lambda arguments: expression

print((lambda x: x**2)(5))  # 25
# call it immediately without storing

x = lambda a : a * 5
print(x(2))


b = lambda x, y : x ** y
print(b(2,5))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you
#  have a function definition that takes one argument, and that argument will be multiplied with an 
# unknown number:

def my_fun(n):
    return lambda a : a * n
doubler_fun = my_fun(5)  #-> will return  lambda a : a * 5
print(f"the anonymous answer is: {doubler_fun(10)}") # here the argument will assign the anonymous parameter of lambda function 



# map(function, iterable) applies a function to each element of an iterable.

# It doesn’t create a new list directly. Instead, it creates a special object called a map object.

# This map object is an iterator → meaning it generates results one by one (saves memory).

# That’s why we usually wrap it with list() or tuple() to see all results at once.

numbers = [1, 2, 3, 4, 5]
map_num = map(lambda x : x ** 2, numbers)
print(map_num)


# numbers = [1, 2, 3, 4, 5,6,7]
# temp = []
# for n in numbers:
#     temp.append(lambda x : x ** 2(n))
# print(temp)


# filter() function 
# filter() function is also a special function in python that is used in each element of iterable like list
# tuple , set etc 
# syntax filter(function, iterable )
# filter() doesn’t modify the original iterable.

# It returns only elements that satisfy the condition (where function returns True).

# If you pass None instead of a function, filter() removes all items that are False 
# in a boolean context (like 0, False, None, "", []).
# use when u want to remove elements that does't stasify condition


integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_int = filter(lambda x : x % 2 == 0, integers)
print(tuple(integers))

words = ["Ai", "Computer", "ML", "SE", "python", "DeepLearning"]
filter_wrds = filter(lambda w : len(w) > 3, words)
print(set(filter_wrds))



# reduce() function
# Think of reduce() as a way to keep combining elements of a sequence into one final result
# by applying a function step by step.

# It’s like folding or compressing a list into a single value.
import functools 
from functools import reduce
nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, nums)
print(f"the sum of element of sequence is: {result}")

rst = reduce(lambda x, y: x + y, nums)
print(f"the sum of all element in list is: {rst}")

max = reduce(lambda x, y: x if x > y else y,nums)
print(f"the maximum number is: {max}")


def fact(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * fact(n-1)
    
num = int(input("Enter any num"))
print(f"factorial of {num} is {fact(num)}")


