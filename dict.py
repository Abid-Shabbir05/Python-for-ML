# Dictionary in Python
# In Python, a dictionary is a built-in data structure that stores data in key-value pairs. 
# It is mutable, meaning you can change its contents, and it allows for fast lookups using keys.
# Creating a Dictionary
# A dictionary is defined using curly braces {} with key-value pairs separated by colons :.
# Key Features of Dictionaries
# Unordered (Python 3.6 and earlier), Ordered (Python 3.7+)
# Keys must be unique and immutable (strings, numbers, tuples)
# Fast lookup using keys
# Dictionaries are widely used in Python, especially in Machine Learning, Data Science, and Web Development.

# Do you want me to give an advanced use case like nested dictionaries or JSON conversion? 

info ={
    "name" : "Abid",  # in dict keys should be unique
    "age" : 23,
    "mark" : [90, 99, 98, 89, 95],
    "course": "Machine Learning",
    "email" : "code.10@gmail.com",
    "topic" : ("dictionary", "set"),
    "is-student" : True,
    3.15 : "pi-value",
    14 : "lucky-num",
    ("reg","id") : "compulsory"  # tuple can use as key b/c it's immuteable unlike list
}
print(info)
print(info["email"]) #this process called look up to get value of given key error
print(info.get("course")) #get() methode use to prevent the keyserrors
info["name"] = "Abid Shabbir"
print(info)
del info["email"] ## Removing a key-value pair
print(info)
print(info.keys()) #return all the keys
print(info.items())  #return all the key's value
print(info.pop(14))
  #remove the spacefic key value pair
info.update({"language" : "python"})  #by this method update(Key : value) insert new key value pair in dict
print(info)

for key, value in info.items():
    print(f" {key} : {value}")


# Empty dictionary
# null_dict = {}
# null_dict["name"] = "abid"
# print(null_dict)  


# nested dictionary

student = {
    "name" : "Shigri",
    "result" : {"eng" : 98, 
                "mth" : 98, 
                "comp" : 99}, #nested dict
    "class" : "4th year"
}
print(len(student))
print(list(student.items())) #here i converted dict into list called typecasting
print(student["result"]["mth"])

# practice
#  Storing Word Meanings in a Dictionary
words_meaning = {
   "table" : ["a piece of furniture", "list of fact and figure" ],
   "cat" : "a small animal"
}
  
print(words_meaning)

# 2
# Finding the Number of Unique Classrooms Needed
# Since each subject needs its own classroom, we can store the subjects in a set (which removes duplicates) 
# and count its length.

sub_list = ["python", "java", "C++", "python", "javascript", "java", "python", "C++", "C", "java"]
unique_sub = set(sub_list)
print(f"total required class room is : {len(unique_sub)}")

# #4 
#  Q =Write a Python program (WAP) to enter marks of 3 subjects from the user and store them
# in a dictionary.
# Start with an empty dictionary and add one by one.
# Use the subject name as the key and marks as the value.

mark1 = int(input("mark of 1st subject is "))
mark2 = int(input("mark of 2nd subject is "))
mark3 = int(input("mark of 3rd subject is "))

Marks = {}
Marks.update({"comp" : mark1})
Marks.update({"math" : mark2})
Marks.update({"eng" : mark3})
print(Marks)


# Solution for Storing 9 and 9.0 as Separate Values in a Set
# Since Python considers 9 (int) and 9.0 (float) as equal in sets,
# we need a workaround to store them separately.

unique_values = set()
unique_values.add((9, "int"))
unique_values.add((9.0, "float"))

print(unique_values)
