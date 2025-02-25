# Conditional statements in Python allow your program to make decisions based on conditions. 
# The main conditional statements are:

# 1️⃣ if Statement
# Executes a block of code only if the condition is True.

n = 18
if n >= 18 :
    print("can vote & apply for license")

# 2️⃣ if-else Statement
# Executes one block if the condition is True, otherwise executes another block.

n = 20 
if n > 20:
    print("able to marry")
else:
    print("not able to marry")
 
# 3️⃣ if-elif-else Statement
# Checks multiple conditions in sequence.

light = "green"
if(light == "green"):
    print("can go")
elif(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("be ready")
else:
    print("system not working")

# 4️⃣ Nested if Statements
# Using an if inside another if.

x = 10
if(x >= 5):
    print(f"{x} is greater than 5")
    if(x >= 8):
        print(f"{x} is also greater than 8")

rst = 90
print("you have passed the exam") if(rst >= 50) else print("sorry try again")

age = 20
print("can vote") if age >= 18 else print("can't vote")

rst = 80
if(rst > 70 and rst <= 80):
    print("You got A grade")
elif(rst <= 70 and rst >= 60):
    print("You got B grade")
elif(rst < 60 and rst >= 50):
    print("You got C grade")
else:
    print("Sorry ! try again")

std = "Abid"
reg = "F23bscs030"

if(std == "Abid" or reg == "F23bscs030"):
    print("you have allowed to enter office")

std = "Ali"
if(not std != "Ali"):
    print("not allowed")


# practice 
num = int(input("Enter any number "))
print(f"Entered number is = {num}")
if(num % 2 == 0):
    print(f"{num} is even number")
else:
    print(f"{num} is odd number ")

n1, n2, n3 = 20, 30, 40
if(n1 > n2 and n1 > n3):
    print(f"{n1} is greatest number")
if(n2 > n1 and n2 > n3):
    print(f"{n2} is greatest number")
elif(n3 > n1 and n3 > n2):
    print(f"{n3} is greatest number")
else:
    print("these numbers are equal")
