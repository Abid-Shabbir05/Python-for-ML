# Tuple in Python
# A tuple in Python is an immutable, ordered collection of elements. It is similar to a list but with
# one key difference: tuples cannot be changed (modified, added, or removed) after creation. 
#  They are defined using parentheses () instead of square brackets [].
# Key Features of Tuples
# Immutable: Once created, you cannot modify a tuple.
# Ordered: The elements have a fixed order.
# Heterogeneous: Can store different data types (e.g., integers, strings, lists, etc.).
# Faster than Lists: Tuples are more efficient than lists in terms of performance.
# Hashable: Tuples can be used as dictionary keys (if they contain only hashable elements).
# Why Use Tuples Instead of Lists?
# Faster: Tuples have better performance than lists.
# Immutable: Prevents accidental modifications.
# Safe: Useful when you want to ensure that data remains unchanged.
# Hashable: Can be used as dictionary keys.
tup = (12,34,54,65,77,23,53)
print(type(tup)) #it return the type of data structure
print(tup)
# tup[1] = 55  Not allowed (immutable)
tup1 = () # is empty tuple
# Tuple with a single element (comma is required)
tup2 = (5,)  # Correct
tup3 = (5)   # Incorrect (interpreted as an integer)
# Creating a tuple without parentheses (tuple packing)
tup4 = 1, 2, 3    # it also called packing tuple  / because python consider the fundamental chratarestic of 
# tuple edfined by comma as well list defined by [] 
print(type(tup4)) # <class 'tuple'>
print(tup4)

# Why Do Lists Need Brackets But Tuples Don't?
# Tuples are immutable, so they can be created simply by separating values with commas.
# Lists are mutable, so Python requires explicit brackets [] to differentiate them from other
# data structures.
tup5 = (12, "Abid", 3.14, True, 34, 90, 12, 34, 12) #hetrogenous tuple 
print(tup5)
print(tup5.count(12)) # it return the occurance of atem in tuple
print(tup5.index("Abid")) # return the the index of item
print(tup5[2 : ]) # slicing is possible in tuple
repeat_tup = tup5 * 2 #it will print repeatedly until the given conditon
print(repeat_tup)
print(len(repeat_tup))

tup6 = (1,2,3)
tup7 = (4,5,6)
new_tup = tup6 + tup7
print(new_tup) # Concatenation


# Checking membership
print(2 in tup6)  # Output: True

import sys

tup = (1, 2, 3)
lst = [1, 2, 3]

print(sys.getsizeof(tup))  # Output: Less memory (e.g., 64 bytes)
print(sys.getsizeof(lst))  # Output: More memory (e.g., 88 bytes)

import timeit

list_test = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)

print("List Time:", list_test)  # Takes more time
print("Tuple Time:", tuple_test)  # Takes less time


# Conclusion
# Commas create tuples
# Parentheses improve readability and are required in special cases
# Empty tuples must have parentheses
# Single-element tuples need a trailing comma
