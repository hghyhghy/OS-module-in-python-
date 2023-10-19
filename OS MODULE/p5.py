# changing the file name by using os module in python

import os

fd = "src/OS MODULE/f1.txt"

# os.rename(fd, "New.txt")

# checking wheather a file  exists

result = os.path.exists("New.txt")

print(result)

file = "New.txt"

f = open(file, "w")

f.write("I am Subham Sarkar")

f.close()


f = open(file, "r")

text = f.read()

print(text)


# printing the size of the file

size = os.path.getsize("New.txt")

print("Size of that file is ", size, "Bytes")


# ctermid() this method returns astring value donoting a file name corresponding the

# controlling terminal of the process

filename = os.ctermid()

print(filename)
