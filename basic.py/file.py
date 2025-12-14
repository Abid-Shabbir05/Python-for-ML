f = open("filetxt.txt", "r") # to open files as a read mode (open for reading is default = r)
data = f.read() # to return entire content as a string
data = f.read(30) # we also spacify the no of characters in a string
print(data) #print the data
print(type(data))

line1 = f.readline() #read one line at a time
print(line1)

line2 = f.readline()
print(line2)


f.close() #  to close the file

# once we read data completly and try to re- read that data then will return empty line because 
# there is nothing left to read 


# ===== for write mode (w)
# open the files in write mode(w) refer to open the files to override or overwrite it will truncate the 
# all previous text and used to  write the new text in a file

with open("filetxt.txt", "a") as f: #file is open as write /with is use to safe handling
    data = f.write("\n this is essential to learn file I/O ") # any data can write into the write methode
    print(data)
# f.close()  is no compulsory when we use with key words for open function


with open("filetxt.txt", "r") as f:# i open file to see the over-write txt
    data = f.read()
    print(data)
f.close()

with open("simple.txt", "a") as f: #in additional when we open file in append(a) and write(w) mode
# python automatically create file 
    f.close()

# everything mean reading and writing done by pointer
# in r+ mode when we write txt it replace from the starting and read where the pointer has stoped
#  after write
with open("filetxt.txt", "r+") as f:
    f.seek(0) #seek( ) is used to move cursor to position where the writing strat form
    f.write("in python ")
    print(f.read())
f.close()


# in w+ mode this will trucate the file first then we can write any txt in the file
with open("filetxt.txt", "w+") as f: # w+ mode open file for read/ write and will truncate
    f.write("in python ")
    print(f.read())
    f.write("hello how are you") 
f.close()


# in a+ mode keep all old content use for read and append except can create new file if not exist
with open("filetxt.txt", "a+") as f: # a+ for read and append
    # f.write("in python ")
    f.write("\nhello how are you") 
    f.seek(0) # can set where the reading start otherwise reading start form current pointer
    print(f.read())
    
f.close()