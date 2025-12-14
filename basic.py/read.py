
f = open("text1.txt", "rt") #to open the file in read mode (t is default )
# data = f.read()
data = f.read(6) # read the character of line by specified number in read method
line1 = f.readline() # use to read single line form the staring (read first line)
print(line1)
line2 = f.readline() # use to read single line form the previous read line (read 2nd line)
print(line2)
lines = f.readlines()# this will give the output in form of list
print(lines)
print(type(lines)) # list
f.close() # close the file