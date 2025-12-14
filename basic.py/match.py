# match
# the match statement is used to perform action based on different condition
# instead of using many if- esle statement we used match statement because it allow one block to execute
# from many

# match expression:
#     case x:
#         print("x")
#     case y:
#         print("y")
#     case z:
#         print("z")


day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    
point = (5 , 0)

match point:
    case(0, 0):
        print("Origin")
    case(x, 2):
        print(f"X-axis at {x}")
    case(0, y):
        print(f"Y-axis at {y}")
    case(x, y):
        print(f"X-axis at {x} and y at {y}")
    case(x, 2):
        print(f"X-axis at {3}")
    
month = 5
day = 3
match day:
    case 1 | 2 | 3 | 5 if month == 3:
        print("weekend in Aprail")
    case 1 | 2 | 3 | 5 |6 if month == 5:
        print("weekend in Aprail")
    case _:
        print("no matching")