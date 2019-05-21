# generate change owed from purchase and deliver in fewest number of coins

from cs50 import get_float
from math import floor


def main():
    while True:
        # Prompt user for valid input (amount of change owed)
        n = get_float("Change owed: ")
        number_of_coins = floor(n * 100)

        if number_of_coins > 0:
            break

    # Always use largest coin possible
    quarters = number_of_coins // 25
    dimes = (number_of_coins % 25) // 10
    nickels = ((number_of_coins % 25) % 10) // 5
    pennies = (((number_of_coins % 25) % 10) % 5) // 1

    # Print final number of coins
    print(f"{quarters + dimes + nickels + pennies}")


if __name__ == "__main__":
    main()