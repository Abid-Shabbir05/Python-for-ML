# in write mode(w) the existing text in the text will tuncate and over write the new text from
# the begging of the text file

f = open("text2.txt", "w") # in write mode(w) if file does't exist then create it automatically
write_data = f.write("Machine Learning is the core parts of Ai") 
f.close()



f = open("text2.txt", "a")# here file is openning in the append mode(a) 
append_txt = f.write("\nso Ml bring many apportunity for the new generation") # so in the appen mode the 
# text will add at the end of the previous page or text the pointer start form the end


f = open("text2.txt", "r+")#r+ mode used to read and write  and over-write the existing text aslo at the 
# stating 
f.write("hoye hoye")
print(f.read())# read form where the writing stoped mean the overwirting parts will not display


f = open("text2.txt", "w+")#w+ mode used to read and write when read the file it open in the truncated mode
f.write("hoye hoye")
print(f.read())

f = open("text2.txt", "a+")#a+ mode used to read and write file
f.write("hoye hoye")
print(f.read())#read form the end of the file


with open("text3.txt", "w") as f: # this the right way to open any file 
    f.write("love love you")

import os
os.remove("simple.txt")
