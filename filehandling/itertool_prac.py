# What is itertools?
import itertools as iter
# A Python module that provides fast, memory-efficient tools for handling iterators (things you can loop over).
# Useful in data processing, combinatorics, machine learning preprocessing, and algorithm design.
# Why is itertools important in ML/DS?
# Efficiently generate feature combinations.
# Handle streaming data.
# Useful for cross-validation and grid search.
# Saves time and memory vs writing loops manually.
# itertools
# It is a built-in Python module.
# It gives you special tools to work with loops and iterators.
# Instead of writing long for loops, you can use itertools functions to do tasks like:
# Repeating things,
# Counting,
# Making combinations/permutations,
# Linking lists together,
# Filtering data efficiently.

# No 1 ## ====== count() ==============================================================]]

# Because count() returns a special iterator object, not a list.
# Printing it directly just shows you what the iterator is (its type and parameters). It doesn’t automatically generate values.
# It creates an infinite counter that generates numbers starting from start and increases (or decreases) by step.
# start → The number to start counting from. (default = 0)
# step → The difference between each number. (default = 1)
counter = iter.count(start=0, step=2)

for i in counter:
    if i > 20:
        break        
    print(i)

# No 2  ## ======= cycle()===================================================================]]
# itertools.cycle(iterable) takes an iterable (like a list, string, or tuple) and repeats its items forever in the same order.
items = ["A", "B", "C"]
repeater = iter.cycle(items)
print(repeater)

# cycle(iterable) alone
# It only repeats items from the iterable forever.
# Each loop iteration gives you just the element.
counter = 0
for val in repeater:
    print(val)
    counter += 1
    if counter == 6:
        break
    
# enumerate(cycle(iterable))
# enumerate() adds a counter/index to each element coming from cycle().
# Each iteration now gives a pair: (index, value).
for i, val in enumerate(repeater):
    if i > 5:
        break
    print(i, val)

# No3 ##============= islice() =========================================================================]]
# islice means “iterator slice”.
# It lets you take only a slice (portion) of an iterator, like cycle, without going infinite.
from itertools import cycle, islice
items = ["A", "B", "C"]
for val in islice(cycle(items), 6):
    print(val)


# No 4 ## ============repeat(object, time = )===============================================]]
# This function repeats the same object over and over.
# object → the thing you want to repeat (a number, string, list, etc.)
# times → (optional) how many times to repeat. If you don’t give it, it repeats forever.
s = "Abid"
repeater = iter.repeat(s, 5)
for val in repeater:
    print(val)



# N0 5##=======itertools.accumulate(iterable, func=operator.add)========================================]]

# accumulate → builds up running totals (or results) from an iterable.
# func → tells how to combine the elements. By default, it uses operator.add (which means normal addition).

# accumulate(iterable, func=operator.add)
# It makes an accumulated result from an iterable.
# By default, it keeps a running total (sum).
# You can also give it a different function (like max, min, operator.mul, etc.) to change how accumulation works.

list1 = [1, 2, 3, 4, 5]
# result = list(accumulate(list1, func=operator.add))
from itertools import accumulate
import operator
result = list(accumulate(list1, func=operator.floordiv)) #//
result = list(accumulate(list1, func=operator.truediv)) #/

print(list(result))

# No 6 ## =======chain(*iterables)============================================================]]

# itertools.chain(*iterables)
# It takes multiple iterables (lists, tuples, strings, etc.) and makes them behave like one single sequence.

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10] 
s = "Abid"
result = iter.chain(list1, list2, s)
print(result) # this will create and iterable object so output === <itertools.chain object at 0x7a2a80fed000>
print(f"combination of list is {list(result)}")


# No ##=======itertools.compress(data, selectors)========================================================]]

# Think of it as a filter:
# data → the items you want to filter.
# selectors → a sequence of True/False values (or 1/0).
# Only the items where the selector is True are kept.


data = ["abid", "ali", "tanveer", "sara", "alia"]
selectors = [True, False , True, True, False]
selectors = [1, 0 , 1, 1, 0]
compressed = list(iter.compress(data, selectors))
print(compressed)

# Suppose we want words longer than 5 letters:

furits = ["Apple", "banana","orange", "dee", "edefd", "ere", "eer"]
selectors = [len(f) > 5 for f in furits]
print("Filtered:", list(iter.compress(furits, selectors)))


# No ##==== itertools.dropwhile(func, iterable)================================]]

# It drops (ignores) items from the start of the iterable as long as the condition is True.
# The moment the condition becomes False, it stops dropping and returns the rest of the items (without checking again).

nums = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10]
drop = iter.dropwhile(lambda x : x < 5 , nums)# drop item form start while condition is true stop when condition become is false
print(f"dropwhile  {list(drop)}")

# No#=========takewhile(func, iterable) → take while condition true.=============================]]

# unlike dropwhile it take item from the iterable until the condition is true stro when false
nums = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10]
drop = iter.takewhile(lambda x : x < 5 , nums) 
print(f"dropwhile  {list(drop)}")

