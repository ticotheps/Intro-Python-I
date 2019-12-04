"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

with open("foo.txt", "r") as fp:
    for line in fp:
        print(line)
        
print(fp.closed) # <== checks to see if 'fp' is closed
        
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

fp = open("bar.txt", "w")

fp.write("line1\nline2\nline3")

# ALTERNATE SOLUTION
# fp.write("""line1
# line2
# line3""")