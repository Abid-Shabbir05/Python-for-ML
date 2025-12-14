# python has the set of buid in math function,including extensive math module that allow you to perform
# mathematical task on number
# Built-in Math Functions
# The min() and max() functions can be used to find the lowest or highest value in an iterable:

list1 = [12, 3, 4, 11, 10, 13, 12]
min_num = min(list1)
max_num = max(list1)
print(f"the smallest number is  {min_num}")
print(f"the greatest number is  {max_num}")

# The abs() function returns the absolute (positive) value of the specified number:
x = -12
pstiv = abs(x)
print(pstiv)

# The pow(x, y) function returns the value of x to the power of y (xy).

a = 5 
a_pow = pow(a, 3)
print(a_pow)



list3 = [1, 2, 3, 4, 5, 6, 7]
max_val = sorted(list3)
print(f"largest element in the list is: {max_val[-1]}")


# find the max value systematically


list4 = [1, 2, 13, 4, 15, 6, 17,18]

max_vl = list4[0]
for num in list4:
    if num > max_vl:
        max_vl = num

print(f"max val is: {max_vl}")






import math

x = 4
sqr = math.sqrt(x)
print(sqr)


