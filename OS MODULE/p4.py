# read write operation by using os module

import os


# storing the file name

fd = "src/OS MODULE/f1.txt"

# opening the file

file = open(fd, "w")  # opening te file in  write mode

file.write("Hello Python")

file.close()

# reading the contents of the file

file = open(fd, "r")  # opening the file in read mode

text = file.read()

print(text)

file.close()
