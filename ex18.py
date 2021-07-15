# this one is like your scripts with argv
# *args takes all arguments and puts them as a list
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
# takes two arguments
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

# call functions with arguments
print_two("Saptarshi","Das")
print_two_again("Saptarshi","Das")
print_one("First!")
# no argumets
print_none()
