# Loop in python
# loop is a repeat instruction that allow to excute a set of code repeatedly till certain condition
# in python we will discuss two type of loop 
# 1: While Loop
# 2: For Loop

# 1: While Loop
# repeat as long as condition true
# while True: it will run for infinite time b/c conditon will never be false
#     print("Hello")

# count = 1
# while count <= 5:
#     print("Hello")
#     # count = count + 1
#     count += 1

# Why we use while loop
# We use a while loop when we don't know in advance how many time we need to iterate,and the 
# loop should continue until a certain condition is met

passward = ""
while passward != "123security":
    passward = input("Enter your passward: ")
    if(passward != "123security"):
        print("wrong!try again")
print("Access successfully! ")


num = 1
while num <= 20:
    print( 2, "*" , num, "=" ,2 * num)
    #  num = num + 1
    num += 1

age = int(input("enter your age: "))
while age < 18:
    print("cannot vote")
    age = int(input("enter your age again: "))
print("can vote")

num = int(input("Enter any number: "))
while num >= 0:
    print(f"{num} is a positive number")
    num = int(input("Enter any number again: "))
print("negative number: stop")

# try:
    # Code that might cause an error
    # risky_operation()
# except ExceptionType:
    # Code to handle the error
    # handle_error()

try:
    result = 10 / 0  # This will cause ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")



while True:  # Infinite loop, will stop when a negative number is entered
    try:
        num = int(input("Enter any number: "))  # Try to convert input to an integer
        if num < 0:  # If negative, stop the loop
            print("Negative number entered. Loop stopped!")
            break  # Stops the loop
        print(f"{num} is a positive number")
    except ValueError:
        print("Invalid input! Please enter a valid number.")  # Handles non-numeric input

# Question:
# Write a Python program that simulates a simple ATM system. The user should enter a correct PIN 
# (1234) to access their account. If they enter the wrong PIN, they should be allowed only 3
#  attempts before the system locks them out.

num = 1
code =1214
print("you have only 3 attemp is allowed ")
while num <= 3:
    try:
        pin = int(input("Enter your pin! ") )  
        if pin == code:
            print("sucessfully access!")
            break
        else:
            print(" you entered wrong pin! ")
            if num == 3:
                print("too many wrong attempt ! try after 24 hours")
            else:
                print(f"Attempt remaining {3 - num}")
            num += 1
    except ValueError:
        print(" string not allowed as a pin ")
    
#     Problem: Number Guessing Game
# The program randomly selects a number between 1 and 10.
# The user has to guess the number.
# If the guess is too high or too low, the program gives a hint.
# The user gets 5 attempts to guess the correct number.
# If they fail in 5 attempts, the program ends and reveals the correct number.    
    
num = 1
target = 5
while num <= 5:
    try:
        user_input = int(input("guss a number between 1 & 10: "))
        if user_input == target:
            print("Wow! you did it great !")
            break
        else:
            if user_input < 3:
                print("Too low! try again " )
            elif user_input > 7:
                print("Too high! try again ")
            else:
                print("good try! you almost there")
            num += 1
    except ValueError:
        print(" I think U entered non_numerical input !")
        break
if num > 5:
    print(f"You have use all five attempt! the correct number is:  {target}")
        
   


        

