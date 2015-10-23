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



# set method cannot contain duplicates

def removeDuplicates(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

print removeDuplicates("tree transversal")
print removeDuplicates("characters")
print removeDuplicates("5521866958")



def removeDuplicate(alist):
    return (list(set(alist))

print removeDuplicates("tree transversal")
print removeDuplicates("characters")
print removeDuplicates("5521866958")
