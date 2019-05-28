"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
print("sys.argv = ", sys.argv)
print("Number of Total Arguments: ", len(sys.argv))
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for i in range(len(sys.argv)):
    print("Command Line Argument #", i+1, ":", sys.argv[i])

# Print out the OS platform you're using:
print("Current OS platform in use: ", sys.platform)

# Print out the version of Python you're using:
print("Current Version of Python in Use: ", sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("Current Process ID: ", os.getegid())

# Print the current working directory (cwd):
print("Current Working Directory: ", os.getcwd())

# Print out your machine's login name
print("My Local Machine's Login Name: ", os.getlogin())
