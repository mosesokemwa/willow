# Using Python, have the function Secondy(lis) take the list of numbers stored in lis
# and return the second lowest and second greatest numbers, respectively, separated by a space.
# For example: if lis contains [7, 7, 12, 98, 106] the output should be 12 98.
# The list will not be empty and will contain at least 2 numbers. It can get tricky if there's just two numbers!



#output: 2nd largest and smallest number
#input: integers with not less than three numbers
#pseudocode:


def Secondy(lis):
	m = lis[:2] #m will hold 2 values, fill it with the first two values of alist
	for num in lis:
		m = sorted(m + [num],reverse=True)[:2] #appends num to m and sorts it, takes only top 2
	print m[1] #the second highest element.

	for num in lis:
		m = sorted(m + [num])[:2] #appends num to m and sorts it, takes only top 2
	print m[1] #the second lowest element is printed out


# keep this function call below here
print Secondy([-45, 0, 3, 10, 90, 5, -2, 4, 18, 45, 100, 1, -266, 706])




#alternate solution

lis = [-45, 0, 3, 10, 90, 5, -2, 4, 18, 45, 100, 1, -266, 706]
print sorted(set(lis))[-2]  #sorts lis in ascending order and takes out duplicate numbers
						   	#returns the second highest value
print sorted(set(lis))[1] 	#sorts lis in ascending order and takes out duplicate)
							#returns the second lowest value
