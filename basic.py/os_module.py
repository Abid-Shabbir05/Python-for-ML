#  What is the os Module?

# The os module in Python provides a way to interact with the Operating System (OS).
# It lets you do tasks like:

# Navigating folders

# Listing files

# Creating/removing directories

# Working with environment variables

# Running system commands

# In short: os connects Python with the system where your code is running.

#  Why & When Do We Need os in Machine Learning?

# In Machine Learning, we usually deal with datasets (CSV, images, text, etc.) stored in folders.
# Here are common cases where os is really useful:

# CSV stands for Comma-Separated Values.
# It’s a plain text file format used to store tabular data (like a spreadsheet) where each line is a row,
# and values are separated by commas.

# 🔹 Beginner Stage (Basic File/Directory Handling)

# These are enough when you’re just starting with datasets.

# os.getcwd() → get current working directory (important to know where your Python file is running).

# os.chdir(path) → change directory (navigate to dataset folder).

# os.listdir(path) → list all files/folders (see dataset files like .csv, .jpg).

# os.path.join(path1, path2) → join paths safely (helps when combining dataset folder + file).

# os.path.exists(path) → check if file/folder exists (good for avoiding errors).

# os.mkdir(path) → create a new folder (e.g., "results").

# os.makedirs(path) → create nested folders (e.g., "outputs/models/v1").



# program
# What is os.getcwd()?
# It returns the path (folder location) where your Python program is running right now.

import os
current_path = os.getcwd()
print(f"your current directory is : {current_path}")


# os.chdir(path) ?
#  What is os.chdir(path)?
# somehow we have to provide full path or directory to read the file inside any 
# folder chdir() just help to will the change the current working directory and helpful
# to specified the file or path that have to read or write

import os  
current_path = os.getcwd() #
print(f"before =  {current_path}")
os.chdir("/home/abidshabbir/Documents")
print(f"After =  {os.getcwd()}")



# os.listdir(path) ?
# os.listdir(path) → Returns a list of all files and folders inside the given directory.
# If you don’t give path, it lists files in the current working directory (os.getcwd()).
# If you give a path, it lists files/folders inside that path.
current_path = os.getcwd() #
print(os.listdir())

for item in os.listdir():
    print(item)



#     os.path.join(path1, path2, ...)
# 👉 Combines multiple parts of a path into one valid path for your operating system.

# It automatically adds the correct / (on Linux/Mac) or \ (on Windows).

# Safer than manually writing "/home/abidshabbir/" + "Documents" (which can break if slashes are missing/extra).

path = os.path.join("home", "abidshabbir","Documents","python","ml")
print(path)

# 2. Join with a filename

base_dir = ("/home/abidshabbir/Documents/python/Python-for-ML")
f_path = os.path.join(base_dir, "Abid")
print(f_path)

# 3. join method
folder = "/home/abidshabbir/Documents/pPath.cwd()ython/Python-for-ML"
filename = "data.txt"
path = os.path.join(folder, filename)

# What it does
# os.path.exists(path) → Checks if a given path (file or directory) actually exists.
# Returns True if it exists.
# Returns False if it doesn’t.

folders =  "/home/abidshabbir/Documents/python/Python-for-ML"
print(os.path.exists(folders))


# create diretroy by using os.mkdir
os.mkdir("result")
print(os.getcwd())


import os

if not os.path.exists("result"):
    os.mkdir("result")
    print("Folder created!")
else:
    print("Folder already exists.")


# What os.makedirs(path) does

# Creates a directory (folder) and all missing parent directories in the path.

# If the folder(s) already exist, it raises an error unless you add exist_ok=True.

# Think of it as:
#  mkdir = make one folder
#  makedirs = make full tree of folders

