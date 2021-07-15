# import argv for command line arguments
from sys import argv

# assign the arg0 to scipt name and the arg1 to input_file name
script, input_file = argv

# function to read a file, takes a file object as argument
def print_all(f):
    print(f.read())

# function to rewind a file, takes a file object as argument
def rewind(f):
    f.seek(0)

# take a line_count and file object and prints a line
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open the input_file
current_file = open(input_file)

# prints the statement
print("First let's print the whole file:\n")

# call print_all function with the current_file object
print_all(current_file)

# print the statement
print("Now let's rewind, kind of like a tape.")

# call rewind function with the current_file object
rewind(current_file)

# print the statement
print("Let's print three lines:")

# assign current_line to 1
current_line = 1
# call print_a_line function with current_line and current_file object
print_a_line(current_line, current_file)

# add 1 to current_line
current_line = current_line + 1

# call print_a_line function with current_line and current_file object
print_a_line(current_line, current_file)

# add 1 to current_line
current_line = current_line + 1
# call print_a_line function with current_line and current_file object
print_a_line(current_line, current_file)
