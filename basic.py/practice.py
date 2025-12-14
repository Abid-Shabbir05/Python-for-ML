# sum the digit of integer by recursive methode

# def sum_int(n):
#     # Base case: if the number has only 1 digit
#     if len(n) == 1:
#         return int(n)
#     else:
#         # Take the first digit + sum of remaining digits
#         return int(n[0]) + sum_int(n[1:]) 

# num = input("Enter any integers: ")
# print(f"sum of the digits of integers {sum_int(num)}")






# def reverse_str(w):
#     if len(w) == 1:
#         return w
#     else:
#         return w[-1] + reverse_str( w[ : -1]) 
# strings = input("Enter any strings: ")
# print(f"reverse form of given string is: {reverse_str(strings)}")



# def reverse_str(w):
#     if len(w) == 1:
#         return w
#     else:
#         return w[-1] + reverse_str(w[:-1])

# strings = input("Enter any string: ")
# print(f"Reverse form of given string is: {reverse_str(strings)}")



# def count(n):
#     if n == 0:
#         print(0)
#     elif n < 0:
#         print("please enter the non-negative number")
#     else:
#         print(n)
#         count(n - 1)

# count()

# def count_sbstr(s):
#     if len(s) == 0:
#         return s
#     else:
#         s[0:2] == s[2:5]
           
       
# S = "machine learner learner"
# count_sbstr(S)


# # # s = "tanveer tan tannuuu"
# # # print(s.count("tan"))



def is_substring(s, sub):
    # Base case: if main string shorter than substring
    if len(s) < len(sub):
        return False
    
    # Check if current slice matches
    if s[:len(sub)] == sub:
        print(s[:len(sub)])
        return True
        
    # Recurse on the rest of the string (drop first char)
    return is_substring(s[1:], sub)
    

# Example usage
print(is_substring("xabcx", "abc"))  # True
print(is_substring("hello", "abc"))  # False
