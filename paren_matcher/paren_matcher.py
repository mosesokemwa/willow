# Write a function that return whether or not the input string has balanced parantheses
# Balanced:
#   '((()))'
#   '(()())'
# Not balanced:
#   '((()'
#   '())('


def paren(str):
	for i in str:
		if i.count("(") == i.count(")"):
			return "Balanced Parenthesis"
		return "Contains unbalanced parenthesis"

print paren("((()))")
