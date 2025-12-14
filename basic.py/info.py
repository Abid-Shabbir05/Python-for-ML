

from functools import reduce 
lists = []
def mul(list):
    # return x * x
    return reduce(lambda a , b : a * b, list)
i = 1
while i <= 5:
    data = int(input("Enter any number:  "))
    e = lists.append(data)
    i += 1

print(f"mul result is  {mul(data)}")