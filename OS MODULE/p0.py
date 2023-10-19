# changing the directory

# importing os module

import os

# creating a function


def ofcreate():
    print("The current working directory is ")

    print(os.getcwd())

    print()


# calling the function

ofcreate()

# changing the directory

os.chdir("../")


ofcreate()
