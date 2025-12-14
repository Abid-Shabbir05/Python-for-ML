# for Loop in python
# A for loop in python is used to iterate over a sequence like{list, tuple,  set, str, dict, etc}
# and execute a block of code multiple time.It is commonly used when we already know how many time the 
# the loop should iterate

# Programs or Practice
nums = [1, 2, 3, 4, 5]
for val in nums:
    print(f" val in num ")

furite = ("Apple", "banana", "caontalope", "orange")
for itm in furite:
    print(itm)

# Using range() in for Loop
# The range() function is useful for generating sequences of numbers.
for i in range(1 , 5, 2): # range(starting , ending, gap)
    print(i)


for val in range(5, 0, -1): #to print itms reversely
    print(f"{val}")

word = "python"
for ltr in word:
    print(ltr)

# Example 4: Iterating Over a Dictionary

student = {"name" : "Abid", "age" : 23, "course" : "ML"}
for key , value in student.items():
    print(f" {key} : {value} ")

# Example 5: Using for with else
# The else block runs when the loop finishes normally (without a break)

for val in range(1, 6):
    print(val)
else:
    print("loop ended")

# Nested Loop
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i = {i} , j = {j}")

#  Controlling for Loop Execution
# 3.1 Using break (Stops the Loop Immediately)

for i in range(0, 5):
    if i == 3:
        print("break point")
        break
    print(i)
    

for i in range(0, 5):
    if i == 2:
        print("mid point") 
        continue #it will skipe the line or set of code if the condition met and continue to the next step 
    print(i)

# when break use else does not run
for i in range(1, 4):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed!")


# using zip( ) to loop over multiple list
# the zip() function allowed you to iterate over multiple list at once
names = ["Arif", "Abid", "Jameel", "Kumail",]
ages = [32, 23, 25, 25]
for name, age in zip(names, ages):
    print(f"{name} is {age} year old")

#  Using for Loop with List Comprehension
# List comprehension is a concise way to create lists using a for loop.

list = [itm ** 1 for itm in range(1 , 5)]
print(list)
    
squre = [itm ** 2 for itm in range(1 , 5)]
print(squre)

sqr_tup = tuple(x ** 2 for x in range(1,5))
print(sqr_tup)

# Looping with enumerate()
# The enumerate() function provides the index while looping over a sequence

vaggies = ["potato", "ginger", "tomato,", "onion", "ladyfinger"]
for index, veg in enumerate(vaggies):
    print(f"at index {index} : {veg}")


# Problems solving
# Sum of First N Natural Numbers
# Problem: Write a program that takes a number n as input and prints the sum of 
# the first n natural numbers.
# n = int(input("enter number: "))
# sum_n = 0
# for i in range(1, n + 1):
#     sum_n += i

# print(sum_n)


# total = 0
# for i in range(1,10):
#     try:
#         num = int(input("Enter any numbers: "))
#         if num == 7:
#             break
#         total += num
#         print(total)
#     except ValueError:
#         print("I think u entered any string instead of numbers")
# print(f"sum of all inputs is: {total}")

# Problem Statement:
# Write a Python program that asks the user to enter N numbers (where N is also provided by the user)
# and calculates the sum and average of these numbers.
while True:
    try:
        total_num = int(input("how many number u want to enter? "))
        if total_num < 0:
            print("enter a positive input")
        else:
            break
    except ValueError:
        print("enter a valid input")
sum = 0
avg = 0
for i in range(1, total_num +1):
    while True:
        try:
            num = int(input("Enter any number! "))
            sum += num
            break
        except ValueError:
            print("this error cause by non_numerical input, correct it! ")
avg = sum/total_num
print(f"sum of all input is: {sum}")
print(f"average of the input is: {avg}")

# Problem Statement:
# Write a Python program that asks the user how many numbers they want to enter. 
# The program should then take that many inputs and find the largest and smallest number among them.

while True:
    try:
        total_input = int(input("how many number you want to enter? "))
        if total_input < 0:
            print("enter a positive number: ")
        else:
            break
    except ValueError:
        print("Enter a Valid input please! ")
nums = []
for i in range(1, total_input+1):
    while True:
        try:
            num = int(input("Enter any numbers!  "))
            nums.append(num)
            break
        except ValueError:
            print("non-numeric value is not allowed! ")

largest = max(nums)
smallest = min(nums)
print(f"the largest number of your inputs is: {largest}")
print(f"the smallest number of your inputs is: {smallest}")
# nums.sort()
# largest = nums[len(nums)-1]
# smallest = nums[0]
    
