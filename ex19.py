# function that takes two arguments and prints few lines
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# print the statement
print("We can just give the function numbers directly:")
# call cheese_and_crackers with 20 and 30
cheese_and_crackers(20, 30)

# print the statemetn
print("OR, we can use variables from our script:")
# assign 10 and 50 to the variables
amount_of_cheese = 10
amount_of_crackers = 50

# call the funtion with the argument assigned above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print the statement
print("We can even do math inside too:")
# call the function with the numbers
cheese_and_crackers(10 + 20, 5 + 6)

# print the statement
print("And we can combine the two, variables and math:")

# call the function with the arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
