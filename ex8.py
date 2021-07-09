# assign formatter the string
formatter = "{} {} {} {}"

# {} is replaced with the values passed as arguments to the .format function
# print 1 2 3 4
print(formatter.format(1, 2, 3, 4))
# print one two three four
print(formatter.format("one", "two", "three", "four"))
# print True False False True
print(formatter.format(True, False, False, True))
# replace formatter with {} {} {} {}
print(formatter.format(formatter, formatter, formatter, formatter))
# print the string seperated by space
print(formatter.format("Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
    ))
