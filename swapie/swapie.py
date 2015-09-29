#Using python, have the function SwapCase(str) take the str parameter
#and swap the case of each character.
#For example: if str is "Hello World" the output should be hELLO wORLD.
#Let numbers and symbols stay the way they are.

#NB do not use the swapcase python method.
import string;

def SwapCase(str):

	new_string = '';
	alphabet_length = len(string.ascii_lowercase);

	for character in str:
		if (character in string.ascii_lowercase):
			for p in range (alphabet_length):
				if (string.ascii_lowercase[p] == character):
					new_string += string.ascii_uppercase[p];
					break;

		else:
			if(character in string.ascii_uppercase):
				for p in range (alphabet_length):
					if (string.ascii_uppercase[p] == character):
						new_string += string.ascii_lowercase[p];
						break;

			else:
				new_string += character;
	return new_string

print SwapCase("The Broom Is TOO LONG FoR no reAson")
