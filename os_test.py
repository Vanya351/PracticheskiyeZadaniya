import os

if not os.path.isdir("folder"):
    os.mkdir("folder")

os.chdir("folder")
print(os.getcwd())

os.rename("text.txt", "newtext.txt")
if not os.path.isdir("folder"):
    os.mkdir("folder")

os.replace("newtext.txt", "folder/text.txt")

for dirpath, dirnames, filenames in os.walk("."):
    print(dirpath, dirnames, filenames)
