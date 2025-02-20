# in this program we will learn abut the operators in python
# Operators in Python are special symbols used to perform operations on variables and values. 
# Python provides several types of operators:
# No:1 Arithmetic Operators (Perform mathematical operations)
# + (Addition), - (Subtraction), * (Multiplication), / (Division)
# % (Modulus), ** (Exponentiation), // (Floor Division)

a = 5
b = 7
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b) #it give reminder afer dividing two numbers
print(a ** 2) #a^2 

#No: 2 Comparison (Relational) Operators (Compare values and return True or False)

# == (Equal), != (Not equal), > (Greater than), < (Less than)
# >= (Greater than or equal to), <= (Less than or equal to)

print(a == b) #False
print(a != b) #False
print(a <= b) #False
print(a >= b) #False
print(a > b) #False
print(a < b) #False

# No 3:  Assignment Operators (Assign values to variables)
# = (Assign), +=, -=, *=, /=, %=, **=, //=

num = 10 #here i assigned 10 as the value of num by using of assignment optr(=)
print(num) #10
num = num + 10 #retrun 20
#or
num += 10 # it give the same result to add new value as num = num + 10
num -= 10
num *= 10
num **= 10

#No 4: Logical Operators (Used for logical operations)
# and (Both conditions must be True)
# or (At least one condition must be True)
# not (Reverses the boolean value)
n1 = 10
n2 = 3
#not
print(not(n1 > n2))
print(not(True))
print(not(False))
#and
v1 = True
v2 = False
print(v1 and v2)
#or
print(v1 or v2)


# Type Conversion
# Implicit Type Conversion (Automatic Conversion)
# Python automatically converts one data type to another when needed.

n1 = 12
n2 = 7.5
sum = n1 + n2 #type conversion 
print(sum) 

a = 2
b = int("9") #type casting
sum = a + b
print(sum)

# In Python, the input() function is used to take user input.
#  It always returns data as a string unless explicitly converted.
# to conver it other type need to use type casting like str(),float(),

# name = input("waht your name")
# print(f"Hellow {name}")

# num = int(input("Enter your number"))
# print(type(num),num)

# Mark = float(input("Enter your number"))
# print(type(Mark),Mark)


#practice 1
num1 = int(input("Enter your First number"))
print(f"number1" ,num1)
num2 = int(input("Enter your 2ns number"))
print(f"number2" ,num2)
sum = num1 + num2
print(f"the sum of two numbers is: ", sum)

#practice 2
len = int(input("Enter the side of squre"))
print(f"area of squre is: ", len**2)