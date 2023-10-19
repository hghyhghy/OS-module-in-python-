# creating a directory using os module in python

import os


# getting the original directory


print(os.getcwd())

# creating a directory

#  giving a name

directory = "Programming"

# writting the parent directory

parentdirectory = " C:/Users/sarka/Desktop/HTMLCSS/MYFIRSTHTML"

# joining the path by using os.patrh.join

path = os.path.join(parentdirectory, directory)

# making the directory by using mkdir ()

os.mkdir(path)

print(os.getcwd())
