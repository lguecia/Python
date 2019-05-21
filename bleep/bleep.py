# censor words

from cs50 import get_string
from sys import argv
import sys
import re


def main():

    # Accepts as its sole command-line argument the name (or path) of a dictionary of banned words (txt file)
        # ex: sys.argv[1] = "banned.txt", path = "/workspace/pset6/bleep/banned.txt"
        # can get key from user and use in line 19: n = (sys.argv[1])

    # Opens and reads from that file the list of words stored therein, one per line
        # f = open("banned.txt") [newline] words = f.readlines()

    # Stores each word in a Python data structure (list or set, i.e words=[]) for later access
    words = set(open(sys.argv[1]).read().split())

    # If no command line argument (e.g., banned.txt) is provided, program exit with a status code of 1
    if len(sys.argv) != 2:
        exit(1)

    # Prompts the user to provide a message
    strings = get_string("What message would you like to censor?")
    print(strings)

    # Tokenizes that message into its individual component words, using the split method on the provided string
    string = strings.split(" ")
    print(string)

    # if the message contained any banned words
    if re.compile('|'.join(words), re.IGNORECASE).search(strings):
        # each of its characters is replaced by a *
        for word in words:
            if strings.isupper():
                word = word.upper()
                strings = strings.replace(word, (len(word) * '*'))
                print(strings)
            else:
                strings = strings.replace(word, (len(word) * '*'))
                print(strings)
    else:
        # Prints back the message that the user provided
        print(strings)


print()


if __name__ == "__main__":
    main()