# Using PYTHON solve the problem below:
# Remove duplicate characters in a given string keeping only the first occurrences.

def removeDuplicates(string):
# Your code here!
	clean = ""
	for i in string:
		if i not in clean:
			clean += i
	return clean
print removeDuplicates("tree transversal")
print removeDuplicates("characters")
print removeDuplicates("5521866958")
