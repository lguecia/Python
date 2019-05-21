# create pyramid using spaces and hashes

from cs50 import get_int


def main():
    # Prompt user for a number between 0 and 23
    while True:
        print("Height: ", end="")
        n = get_int()
        if n > 0 and n <= 23:
            break

    # Print out this many spaces and hashes
    for i in range(n):
        print(" " * (n-i-1), end="")
        print("#" * (i+1))


if __name__ == "__main__":
    main()