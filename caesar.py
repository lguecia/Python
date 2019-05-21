# encryption

from cs50 import get_string
import sys


def main():
    # Check if the user entered 1 command line arguments
    if len(sys.argv) != 2:
        print("You did not enter the correct number of command line arguments")
        exit(1)

    # Get the key from the user
    key = sys.argv[1]

    # Convert string to integer
    key = int(sys.argv[1])

    # Get the plaintext
    plaintext = get_string("plaintext: ")
    print("ciphertext: ", end="")

    # Encipher plaintext. If alphabetic, preserve case and shift it by the key. Print ciphertext back to the user
    for p in plaintext:
        if p.islower():
            print(chr(((ord(p) - 97 + key) % 26) + 97), end="")
        elif p.isupper():
            print(chr(((ord(p) - 65 + key) % 26) + 65), end="")
        else:
            print(p, end="")
    print()


if __name__ == "__main__":
    main()