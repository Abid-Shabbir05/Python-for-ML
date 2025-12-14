# In Machine Learning (ML), operators are essential because they help manipulate data, 
# perform computations, and implement algorithms efficiently.
# membership operator in python are use to test weather a value or element is presented in sequence 
# such like that (list , tuple , set, dict etc)

#
# num = [1, 2, 3, 4, 5, 6, 7]
# print(1 in num)




# furit = ["apple", "banana", "orange", "pineapple"]
# print("mango" not in num)

# the membership is use to confirm is any element is presented in sequence or not



# logical not operator is used to confrim the inverse of desired result means if the expression is true
# retrun false if the expression is false then it retrun true

# n = int(input("Enter any number!  "))

# if not n % 2 == 0:
#     print(f"{n} is not Even number")
# else:
#     print(f"{n} is the Even number")


# password = input("Enter your password!")
# if not password == "abid123":
#     print("you entered a wrong password! ")
# else:
#     print("Access granted! ")


# is_raining = True

# if not is_raining:
#     print("you can travel")
# else:
#     print("better stay indoor")


# indentity operator identity operator are used to compare the memory location of two object not
# their value
# python has two indentity operator
# (is and is not )retrun True when an immuteabe like variable tuple with short leng have the same value then they share
# same memory location

# a = 5
# b = 5
# print(a is b)  # return True
# print(a is not b) # return False


# # muteable
list1 = [1]
list2 = [1]
print(list1 == list2)
print(list1 is list2)
print(list1 is not list2)

# Python never automatically reuses memory for mutable objects, because if it did, 
# changing one variable would unexpectedly change the other.


# bitwise operator



# Bitwise Operators in Python

# Bitwise operators work at the binary level, manipulating individual bits of integers.

# Python has six main bitwise operators:



a = 5
b = 4
print(a ^ b)

print(a & b)

print(a | b)


# leftshift
a = 5
print(a << 1) # shift left by one bit,(multiply by 2 means a * 2^1)
# output = 10

# rightshif
a = 20
print(a >> 2) #shift right by two bit, divided by 4 means a/2^2

# output = 5



# if i have to divide each element of list by 4 then 


n = [1,12, 3, 4, 6, 56]
n_map = map(lambda x : x >> 2, n)
print(list(n_map))
