# create a new file "practice.txt" in pyton add the following data in it
# and write a function to replace a spacific words 



# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)
#     rep_data = data.replace("java", "python")

# with open("practice.txt", "w") as f:
#     f.write(rep_data)




# to find substring in file 
# sub_str = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if sub_str in data:
#         print("found the substring")
#     else:
#         print("not found")




# def check_substr():
#     sub_str = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if sub_str in data:
#         print("found the substring")
#     else:
#         print("not found")

# check_substr()


# write a function to find in which line the words "learning " occur first

# sub_str = "learning"
# with open("practice.txt", "r") as f:
#     data = f.readline(8)
#     if sub_str in data:
#         print("yes occur in first")
#     else:
#         print("not occur in the first of line")


# with open("number.txt","w") as f:
#     f.write(
#     )

# sub_str = "python"
# with open("practice.txt", "r") as f:
#     line1 = f.readline(6)
#     f.readline()
#     line2 = f.readline(6)
#     f.readline()
#     line3 = f.readline(6)
#     f.readline()
#     line4 = f.readline(6)
#     if sub_str in line1:
#         print("found first in line 1")
#     elif sub_str in line2:
#         print("found first in line 2")
#     elif sub_str in line3:
#         print("found first in line 3")
#     elif sub_str in line4:
#         print("found first in line 4")
#     else:
#         print("please enter the valid string")




# def check_sbstr():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(f"found in line number {line_no}")
#             line_no += 1

# check_sbstr()


with open("num.txt", "w") as f:
        f.write("1,2,3,4,5,6,7,8,9,10,11,12,13,14")



# from a file containing number seprated by comma,print the count of even numbers

count = 0
with open("num.txt", "r") as f:
        data = f.read()
        num = data.split(",")
        for val in num:
            if int(val) % 2 == 0:
                # print(val)
                count += 1
print(count)




# def count_even_numbers(filename):
#     count = 0
#     with open(filename, "r") as f:
#         data = f.read()              # read full content as string
#         numbers = data.split(",")    # split by comma into list

#         for val in numbers:
#             if int(val) % 2 == 0:    # check even
#                 count += 1

#     return count


# # call the function
# result = count_even_numbers("num.txt")
# print("Total even numbers:", result)



    





   
