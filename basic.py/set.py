# Python Sets: A Powerful Data Structure
# A set in Python is an mutable and unordered collection of unique elements. 
# It is useful when you need to store distinct items and perform operations 
# like union, intersection, and difference efficiently.
# Sets are created using curly braces {} or the set() function.
# What Can Be Stored in a Set?
# ✔ Integers (int)
# ✔ Floating-point numbers (float)
# ✔ Strings (str)
# ✔ Tuples (tuple) (because they are immutable)
#  What Cannot Be Stored in a Set?
#  Lists (list) –  Mutable, so not hashable
#  Dictionaries (dict) – Mutable, so not hashable
#  Another Set (set) –  Mutable, so not hashable

# practical by programs
furit = {"Apple", "Orange", "Pear", "Peach", "Grapes"}
print(furit)
print(type(furit))

my_set = {1, 3.14, "Hello", (10, 20)}
print(my_set)

# Empty set
empty_set = set()
empty_set.add(10)
print(empty_set)  # Output: {10}

# OR can creat a set using set function set()

color = set(["Red", "Green","Yellow","Yellow"]) #set don't eccept copy or iterate of same items so it take unique one
print(color)

# Accessing Elements in a Set
# Since sets are unordered, we cannot use indexing like lists. Instead, we check for 
# the presence of an item using the in keyword.
if "Red" in color:
    print("yes !Red is in the color set")

# Adding and Removing Elements
# we can add any item in a set by add() function
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(numbers)
# Removing Elements
# there is two way to remove item from set remove() and discard()
numbers.remove(6) # Removes 6, raises an error if not found
print(numbers)
# numbers.remove(10) #here it return key error so to prevent it we used discard b/c
numbers.discard(10) #Removes 10 if it exists, otherwise does nothing
print(numbers)
# pop method
print(f" before pop method: {numbers} ")
pop_num = numbers.pop() #Removes and returns a random element
print(f"After pop method: {pop_num}")
print(f" After  pop method: {numbers} ")

# Set Operations (Union, Intersection, Difference)
# Sets are powerful for mathematical operations like union, intersection, and difference.

# Union (|) → Combines elements from both sets
A = {10, 11, 12,15}
B = {12, 13, 14, 15}
# union = A.union(B) 
union = A | B
print(f"Union of A and B set is : {union}")

# Intersection (&) → Common elements in both sets
# intersec = A.intersection(B)
intersec = A & B 
print(f"intersection of A and B set is : {intersec}")

# Difference (-) → Elements in A but not in B
# dif = A.difference(B)
dif = A - B
print(f"the difference between A/B is : {dif}")

# Symmetric Difference (^) → Elements in A or B, but not both
A.symmetric_difference(B)
# OR
Symtric_dif = A ^ B
print(f"symmetric difference between set A and B is : {Symtric_dif}")
