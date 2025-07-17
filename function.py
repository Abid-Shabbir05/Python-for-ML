# function is very essential to reduce the code redundancy in program 
# a =3 , b = 4
# sum = a + b
# print(sum)

# a =3, b = 4, c = 5
# sum = a + b = c
# print(sum)

# a = 13, b = 14, c = 5
# sum = a + b = c
# print(sum)

# here for the same operation we have to repeat the same line of code again and again
# and this will reduce ur code quality , accuracy, correctness, and formate etc, so to prevent this 
# of mistake and useless effort function is very important when we have to perform multiple same type of
# operation ,instead the above way we use function here ok

# def cal_sum(a,b): # fuction is defination or initiallization
#     return a + b # send back the result to the function caller

# print(cal_sum(4, 5)) #function call
# print(cal_sum(14, 15))
# print(cal_sum(14, 5))
# print(cal_sum(1, 5))


# Default arguement

# def cal_mul(a =1, b = 2): #this call default argument which is assigned in the function defination
#     return a * b
# mul = cal_mul(4, 5) #funtion always use the arguments which pass during function call even default is given
# print(mul)

# # write a program to print the length of list by using the function 

# def len_list(n_list):
#     return len(n_list)

# list1 = [1,2,3,4,5,6,12,23,55,6]
# n = len_list(list1)
# print(f"the length of list is: {n} ")


# write a function to print the element of list in a single line

# furite = ["Apple", "Mango", "Grapes", "Pears", "Banana"]
# def list_items(items):
#     for item in items:
#         print(item, end= "")
# list_items(furite)


# enumerate funcion is used to print the items of list with the indices to make the output more readable

# menu = ["Pizza", "Burger", "Fries"]
# for index, items in enumerate(menu, start=1):
#     print(f"{index}.  {items}")


# WAF to find the factorial of  any number
# def factorial(n):
#     return n(n-1)
# print(factorial(5))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# num = 5
# result = factorial(num)
# print(f"the factorial of {num} is {result}")

# def factorial(n):
#     r = 1
#     if n == 0 or n == 1:
#         return 1
#     for i in range(1, n+1):
#         r = r * i
#     return r
# num = 10
# fact = factorial(num)
# print(fact)

# WAF to convert USD in Pak Rupee

def converter(usd):
    pak_rup = usd * 280
    print(f"{usd}$ = {pak_rup} Pkr")
converter(100)