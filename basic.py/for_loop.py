# we use for loop when we already know the exact no of iteration over the sequence (list, tuple, string, array) or
# for loop is useful when the number of iteration is countable or already know and for loop is suitable 

# write a multiplication table of 7 using for loop

num = 7

for i in range(1, 21):
    table = num * i 
    print(f"{num} x {i} = {table}")

# print all element of list
colors = ["red", "green", "blue", "yellow"]

for item in colors:
    print(item)


# write a program to pringt all number form 1 to 20 divisible by 3

for i in range(1, 21):
    if i % 3 == 0:
        print(f"{i} is divisible by 3")
    else:
        print(f"{i} not divisible by 3")


# write  a program in a way where the output cover in single or double line instead of line by line

divisible = []
not_divisible = []

for i in range(1, 21):
    if i % 3 == 0:
        divisible.append(str(i))
    else:
        not_divisible.append(str(i))

print(f" {", ".join(divisible)} is divisible by 3")
print(f" {", ".join(not_divisible)} is not divisible by 3")