import os

# Create two test files
# with open("file1.txt", "w") as f:
#     f.write("This is file1.")

# with open("file2.txt", "w") as f:
#     f.write("This is file2.")

# print("Before renaming/replacing:")
# print("file1.txt and file2.txt are created.\n")

# # --- Using os.rename() ---
# try:
#     os.rename("file1.txt", "file2.txt")  # Trying to rename to an existing file
# except FileExistsError:
#     print("os.rename()  FileExistsError: 'file2.txt' already exists")
# except OSError as e:
#     print(f"os.rename()  OSError: {e}")

# # --- Using os.replace() ---
# try:
#     os.replace("file1.txt", "file2.txt")  # This will overwrite file2.txt
#     print("os.replace() file1.txt replaced file2.txt successfully")
# except Exception as e:
#     print(f"os.replace()  Error: {e}")


# os.stat(path)

# Returns detailed info about a file.

# You get metadata like:

# File size

# Permissions

# Creation, access, modification time
import time

# # Create a sample file
# with open("sample.txt", "w") as f:
#     f.write("Hello, Abid!")

# # Get file information
# info = os.stat("sample.txt")
# print(info)
# print("File Size:", info.st_size, "bytes")
# print("Created:", time.ctime(info.st_ctime))
# print("Last Modified:", time.ctime(info.st_mtime))
# print("Last Accessed:", time.ctime(info.st_atime))


# os.environ

# Represents the environment variables of your system (like PATH, HOME, etc.).
# You can read, update, or set environment variables from Python.

# What is an Environment Variable?

# An environment variable is like a global setting/value stored in your operating system that programs can use while running.

# It’s basically key–value pairs that store important configuration info.

# PATH → tells the system where to look for installed programs.

# HOME (Linux/macOS) or USERPROFILE (Windows) → your user’s home directory.

# TEMP → where temporary files are stored.

# PYTHONPATH → where Python should look for modules.
import os

# Print all environment variables
print("All environment variables:")
for key, value in os.environ.items():
    print(f"{key} = {value}")

# Access a specific variable
print("\nHOME directory:", os.environ.get("HOME"))

# Set a new environment variable
# os.environ["MY_VAR"] = "Abid_123"
# print("MY_VAR =", os.environ["MY_VAR"])


