# pathlib is a standard Python module (built-in since Python 3.4) for working with file system paths.
# It provides an object-oriented approach to handling files and directories, unlike the older os and os.path modules.
# In pathlib, a path is an object (Path object), not just a string.
# This object comes with built-in methods and attributes that make it behave like a real-world "Path" entity
#  Most Useful for ML

# If I had to shortlist top 7 you’ll use a lot in ML projects:

# Path.cwd() / Path.home() → to set base paths.

# path / "subdir" → to build dataset/model paths.

# .exists(), .is_file(), .is_dir() → to check dataset/model availability.

# .mkdir(parents=True, exist_ok=True) → to create folders for data/models/logs.

# .glob() / .rglob() → to iterate datasets (images, csvs, etc.).

# .read_text() / .write_text() → for logs, configs, experiment results.

# .name, .stem, .suffix, .parent → to extract dataset file info.

# Why use pathlib?

# Compared to os and os.path, it is:

#  Cleaner & more readable → path / "subdir" / "file.txt" is better than os.path.join(path, "subdir", "file.txt").

#  Cross-platform → Automatically handles Windows (\) and Linux (/) style paths.

#  Feature-rich → Makes common tasks like reading, writing, checking existence, or iterating through files much simpler.

#  Object-oriented → Paths are objects, so you can chain operations.

from pathlib import Path
print(f"your current working directory is: {Path.cwd()}") # retrun current working directory
print(f"your current working directory is: {Path.home()}") #base path

# . Path()
# Creates a path object (not a real folder or file).
# It can be absolute or relative.
# print(Path.cwd)
path_object = Path("/home/abidshabbir/Documents/python/Python-for-ML/filehandling")
print(path_object)
sub_path = path_object / "image"
print(sub_path)

sub_path.mkdir()


from pathlib import Path
path = Path("/home/abidshabbir/Documents/python/Python-for-ML/filehandling")
check_path = path.exists() # to check weather a file or folder is exist or not
print(check_path)


file_path = Path("practice.py")
check_file = file_path.is_file()#to check weather the file exist or not = file specifically
print(check_file)

dir_path = Path("/home/abidshabbir/Documents/python/Python-for-ML")
check_dir = dir_path.is_dir() #weather the directory is exist or not
print(f"is this directory exist {check_dir}")

#  The .mkdir(parents=True, exist_ok=True) pattern is the standard way in ML projects to make sure
# your required folders exist before saving datasets, models, or logs.
# Define project structure
data_dir = Path("project/data")
model_dir = Path("project/models")
log_dir   = Path("project/logs")

# Create folders (if not already present)
for folder in [data_dir, model_dir, log_dir]:
    folder.mkdir(parents=True, exist_ok=True)


# glob()
# Looks for files only inside one folder.
# It does not go inside subfolders.
folder = Path("/home/abidshabbir/Documents/python/Python-for-ML/filehandling")
for f in folder.glob("*.py"):
    print(f)

# rglob()
# Looks for files inside the folder AND all subfolders.
# It goes “deep” and checks every folder inside.
older = Path("/home/abidshabbir/Documents/python/Python-for-ML/filehandling")
for f in folder.glob("*.py"):
    print(f)


text_file = Path("text1.txt")
read_file = text_file.read_text()# it read the content of text file
print(read_file)

text_file = Path("/home/abidshabbir/Documents/python/Python-for-ML/filehandling/text1.txt")
print(Path.cwd()) #
print(text_file.write_text("hello I am mr abid "))