# Given a roman numeral as input, write a function that converts the roman
# numeral to a number and outputs it.
#
# Ex:
# translateRomanNumeral("LX") # 60
#
# When a smaller numeral appears before a larger one, it becomes
# a subtractive operation. You can assume only one smaller numeral
# may appear in front of larger one.
#
# Ex:
# translateRomanNumeral("IV") # 4
#
# You should return `nil` on invalid input.


def romanNumeral(string):
	values = {"i":1, "v":5, "x":10, "l":50, "c":100, "m":1000}


	return sum(map(lambda x: values[x], string))
print romanNumeral("vxiilm")


#map(func, seq) is a function with two arguments
#Lambda functions are mainly used in combination with the functions filter(), map() and reduce()

