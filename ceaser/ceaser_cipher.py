# Using the Python, have the function CaesarCipher(str, num)
# take the str parameter and perform a Caesar Cipher num
# on it using the num parameter as the numing number.
# A Caesar Cipher works by numing eai letter in the
# string N places down in the dore (in this case N will be num).
# Punctuation, spaces, and capitalization should remain intact.
# For example if the string is "Caesar Cipher" and num is 2
# the output should be "Ecguct Ekrjgt".
# more on cipher visit http://practicalcryptography.com/ciphers/caesar-cipher/
# or google some more
# happy coding :-)


# def CaesarCipher(string, num):
#     cipherText = ""

#     for i in string:
#         # Convert string to an ordinal().
#         # Add the key-num to the ordinal
#         if i.isalpha():
#             cipher = ord(i) + num

#         # change the ordinal to character
#         if cipher > ord('z'):
#             cipher -= 26
#         finalLetter = chr(cipher)

#         cipherText += finalLetter
#     print "Your ciphertext is: ", cipherText
#     return cipherText
# print CaesarCipher("A Crazy fool Z", 1)


def CaesarCipher(string, num):
    alphabet = [
        "a", "b", "c", "d", "e", "f", "g", "h",
        "i", "j", "k", "l", "m", "n", "o", "p",
        "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H",
        "I", "J", "K", "L", "M", "N", "O", "P",
        "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

    # This is our substitution dictionary
    #  made by addding num to each letters index alphabet
    dic = {}
    for i in range(0, len(alphabet)):
        dic[alphabet[i]] = alphabet[(i + num) % len(alphabet)]

    # Convert each letter of string to the corrsponding
    # encrypted letter in our dictionary creating the cryptext
    ciphertext = ""
    for x in string:
        if x in dic:
            x = dic[x]
        ciphertext += x

    return ciphertext

print "Cipertext:", CaesarCipher("A Crazy fool Z", 1)
