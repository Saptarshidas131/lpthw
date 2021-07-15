# import argv for commmand line arguments processsing
from sys import argv

# assign argv1 to script and argv2 to filename
script, filename = argv

# print the lines
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# open the filename in write mode and create a file object to target
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# empty the file
target.truncate()

# print the statements
print("Now I'm going to ask you for three lines.")

# take 3 input lines
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# print the line
print("I'm going to write these to the file.")

# write the lines to the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# close the file
target.close()
