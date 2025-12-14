# Error Handling / Exception in Python

# When your Python program runs into a problem (like dividing by zero, using a wrong index, or opening a missing file), it raises an exception.

# If you don’t handle it → the program stops with an error.
# If you handle it → the program can recover or continue running safely.

# This process of dealing with errors is called error handling (or exception handling).

# x = 10
# y = 0
# try:
#     print(x/y)
# except:
#     print("you cannot divide by zero")


# try:
#     num = int(input("Enter any number:  "))
#     r = 10/num
#     print(r)
# except ZeroDivisionError:
#     print("you cannot divide by zero! ")
# except ValueError:
#     print("Enter a valid number!")
# else:
#     print("nothing went wrong")
# finally:
#     print("Execution is compeleted!")


try:
    num = [1, 2, 3, 4, 5]
    print(num[6])
except Exception as e:
    print("An error is occoured: ", e)
else:
    print("no error")
finally:
    print("execution is compeleted")