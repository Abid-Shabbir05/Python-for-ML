# I think you meant functools module (not funtools) .
# It’s a built-in Python module that provides higher-order functions — functions that act on or return other functions. 
# It’s mainly used for function manipulation, optimization, and functional programming patterns.
# Mainly used to make functions more powerful, reusable, and optimized.

# ================reduce(func, iterable)=====================================

# What is functools.reduce?
# reduce takes a function and an iterable (list, tuple, etc.).
# It reduces the iterable into a single value by applying the function step by step.
import functools as fun
import operator
list1 = [1, 2, 3, 4, 5]
result = fun.reduce(operator.mul, list1)
# result = fun.reduce(lambda x,y : x * y, list1)

print(f"the final answer  {result}")