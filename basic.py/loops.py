
# i = 1
# while i < 6:
#     if i == 3:
#         print("achived the target")
#         break
#     i += 1


# print all the even and odd number between 1 and 50

# i = 1
# while i < 50:
#     if i % 2 == 0:
#         print(f"{i} is the even number")
#     else:
#         print(f"{i} is the odd number")
#     i += 1

# print sum of first 20 natural number
# n = 1
# sum = 0
# while n <= 20:
#     sum = sum + n
#     n += 1
# print(f"sum of first 20 number is {sum}")

# factorial of a number
# n = int(input("Enter any number: "))
# fact = 1
# i = 1
# while i <= n:
#     fact = fact * i
#     i += 1
# print(f"factorial of {n} is {fact}")

# write a program to check the correct password
# password = "key25"
# key = 1
# while key <= 5:
#     user_input = input("Enter you password! ")

#     if user_input == password:
#         print("Now you can access! ")
#         break
#     else:
#         print("Wrong password try again!")
#     key += 1
# if key > 5:
#     print("to many attempts! Access denied")
    
    
# Reverse the digit of give number
# input_num = int(input("Enter any squence of number! "))
# reverse_num = input_num[ ::-1]  #this reverse the give sequence of input 
# print(reverse_num)

# input_num = int(input("Enter any squence of number! "))
# rev = 0
# while rev < 0:
#     digit = input_num % 10 # this will get the last digit
#     rev = rev * 10 + digit # build the reverse
#     input_num = input_num // 10 # remove the last digit
# print(f"reverse number is {rev}")


input_num = int(input("Enter any sequence of numbers! "))
reverse_num = 0
while input_num > 0:
    digit = input_num % 10 # this will get the last digit or (reminder after divsion by 10)
    reverse_num = reverse_num * 10 + digit # build the reverse number 
    input_num = input_num // 10 #this will remove the last digit or (will get the qutient except reminder)
print(f"the reverse of sequence of integers is {reverse_num}")
