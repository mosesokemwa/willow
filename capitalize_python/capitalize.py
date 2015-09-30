# Using ruby, have the function capitalize(str) take the str parameter being passed and capitalize
# the first letter of each word. Words will be separated by only one space.
# it should take string input from a user
# do not use the capitalize method


import sys


def main():
    with open(sys.argv[1], "r") as f:
        for line in f:
            print(' '.join(map(lambda e: e[0].upper() + e[1:], line.rstrip().split())))

if __name__ == "__main__":
    main("jungle heaven")
