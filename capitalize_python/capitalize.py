# Using ruby, have the function capitalize(str) take the str parameter being passed and capitalize
# the first letter of each word. Words will be separated by only one space.
# it should take string input from a user
# do not use the capitalize method


def upperfirst(x):
    return x[0].upper() + x[1:]


x = input("Enter a sentence: ") #raw_input was changed to input in python 3.4.3
while x == "":
	x = input("Enter a sentence: ")
else:
	print (x)

y = upperfirst(x)
print(y)





