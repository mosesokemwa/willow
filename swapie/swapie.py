# Using python, have the function SwapCase(str) take the str parameter
# and swap the case of each character.
# For example: if str is "Hello World" the output should be hELLO wORLD.
# Let numbers and symbols stay the way they are.

# NB do not use the swapcase python method.

import string


def SwapCase(str):

	# initialize an empty list
	new_string = '';

	# asigning
	alphabet_length = len(string.ascii_lowercase);

	# looping through string
	for character in str:

		# checking whether string contains lower case
		if (character in string.ascii_lowercase):
			for p in range (alphabet_length):

				# turning lowercase letters to uppercase
				# adds new uppercase letters to the list new_string
				if (string.ascii_lowercase[p] == character):
					new_string += string.ascii_uppercase[p];
					break;

		else:
			# checking whether string contains upper case letters
			if(character in string.ascii_uppercase):
				for p in range (alphabet_length):

					# turning uppercase letters to lowercase
					# adds new lowercase letters to the list new_string
					if (string.ascii_uppercase[p] == character):
						new_string += string.ascii_lowercase[p];
						break;

			else:
				# this should account for the non letter items
				new_string += character;
	return new_string

print SwapCase("It DOeS nothing to INTEGRs like 662258793, @Booleans & WierD")