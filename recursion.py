# so recursion is the methode of solving the sub version of any large problem by repeatedly call the 
# function itself
# for example factorial

def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

num = 5
print(f"the factorial of {num} is : {factorial(num)}")


# another example is 

def num(n):
   if n == 0:
       return
   print(n)  
   num(n-1)
n = 5
print(num(n))

# fibonacci sequence
# fibonacci is the series of number where each number is the sum of its two previous ones
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) +fibonacci(n-2)
num = 10
print(f"fibonacii of {num} is {fibonacci(num)}")


# another methode
def fibonacci(n):
    a , b = 0, 1
    for _ in range(n): 
        a, b = b , a + b
    return a
print(fibonacci(5))

# The underscore _ is a valid variable name in Python — just like i, j, x, etc.

# But it has a special meaning in this context:

# It tells Python (and humans) “I don’t care about this value.”

# recursive function to sum of first n natural number
def sum(n):
    if n <= 0:
        print("natural no is not start form 0")
    elif n == 1:
        return 1
    else:
        return n + sum(n - 1)
num = 5
print(f"the sum first {n} natural number is {sum(num)}")


# write a recursive function to print the element of list 
book = ["English", "Math", "Computer", "Science", "islamiat"]

def list_items(idx, item):
    if idx < len(item):
        print(item[idx])
        list_items(idx + 1, item)
    # for itm in items:
    #     print(itm)
list_items(0,book)