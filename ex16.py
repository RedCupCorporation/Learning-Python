from sys import argv # importing arguments

script, filename = argv # assigning variable names to the arguments

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") # here we don't assign a variable to raw_input because it's just to determine whether or not to continue

print "Opening the file..."
target = open(filename, 'w') # opens filename from the arguments and assigns the contents to target

print "Truncating the file.  Goodbye!"
target.truncate() # erases the file

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ") # we assign variables for the raw_inputs here because we plan on using them later
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it."
target.close()

print "Would you like to read the file you just created? CTRL-C if not"
raw_input("?")

print open(filename).read()
# file = open(filename)
# print file.read()
