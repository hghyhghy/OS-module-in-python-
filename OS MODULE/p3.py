# deleting a file or directory by using python os module


import os

# giving the file name

file = "file1.txt"

loaction = r"C:\Users\sarka\Desktop\HTMLCSS\MYFIRSTHTML>"

print(os.remove("src/OS MODULE/file1.txt"))

# approach 2 by using removedir

print(os.removedirs("src/OS MODULE/file1.txt"))


# os.name ()  this function gives the name of the os dependent module imported

print("The os name is ", os.name)
