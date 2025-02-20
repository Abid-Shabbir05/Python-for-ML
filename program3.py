# In Python, a string is a sequence of characters enclosed in either 
# single ('), double (") or triple (''' or """) quotes.Strings are immutable,
# meaning they cannot be changed after they are created.
                                                                           
s1 = "Hellow world"
s2 = 'hellow world'
s3 = """Hellow world 
          wellcome to Machine learning """ #the oftenly use multiple line string

# No 2 Concatenation (+) 

s = s1 + " " + s2
print(s)

# No 3. Repetition (*)

s = "Hellow"
print((s + " ") * 3)

# No 4 3. Indexing (Accessing Characters)
s = "Python"
print(s[0])
print(s[-1])

# No 5. Slicing (Extracting Substrings)

s = "Now I am learning Machine Learning"
print(s[0:4]) # it we cut the substring according to index including the first 0,and till 4 but 4 itself not include
print(s[:12]) #it by default start from 0 index
print(s[4:7]) #blank space also assigned with index
print(s[-1]) #last string
print(s[0:]) # it will print all because limit index is not fixed here
print(s[-14]) #it will start from last index or backward
print(s[-14:])

# String Methods
# Python provides various built-in methods for string manipulation.

# No Convert Case
s = "hey Abid is Here"
print(s.lower()) # it change all each letters in lower case
print(s.upper()) #it change all each letters in upper case
print(s.title()) # it change every first letters of each words into a uppercase
print(s.capitalize()) #it only chang the first letter of the sentence into a uppercase

# . Checking for Substrings
# two  keywords use for check the existance of substring in or not in (return True / False)
s = "Machine learning"
print( "Machine " in s) # True
print( "Machine " not in s) #False
print( " Web " in s) #False

# 3. Finding Substrings
# in it is also finding the substring but it return the index of substring if it is exist
# keyword = find("substring")

s = "Inshallah today we will complete this chapter"
print(s.find("Inshallah")) #it give the starting index of substring
print(s.find("Abid")) # if substring not found then return -1

# 4. Replacing Substrings 
#  replace(previous word,new word) keyword is use here to replace any substring in strings

s = "I love python"
new_s = s.replace("python","Machine Learning")
print(new_s)

# 5. Splitting and Joining Strings
# here we use two key words split() and join(words) 

s = "Machine Learning is fun"
words = s.split()
print(words) # it siplit each substring by comma 
joined = "-".join(words) # here a bit logical to joine but easy output-> {Machine-Learning-is-fun}
print(joined)
s = "Are u coder ?"
merge = "-".join(s)
print(merge) 


# Escape Sequences
# Escape sequences are used for special characters.
s = "this is an \n AI " #for new line \n
print(s)

s = "build code to predict:\t What Next" #Tab
print(s)

s = "She said, \"Python is great!\""  # Using quotes (\")
print(s)

# String Formatting
# using format()
name = "Abid"
age = "22"
formated = "My name is {} and age is {}".format(name,age) 
print(formated)

# 2. Using f-strings (Python 3.6+)
name = "Abid"
age = 25
msg = f"My name is {name} and I am {age} years old."
print(msg)

#len() used to find the length of strings

# endwith()function
print(name.endswith("d"))# return Ture or False

# cout()function 
# it is use for count the occurance of substring
s = "Make your dream is a reality"
print(s.count("a")) # 4


# Practice hour
nam = input("Enter ur name: ")
print(f" length of name is: {len(name)}" )

str = "I have 100$ and want to give u 50$"
print(f"occurance of sub str is: {str.count("$")}")