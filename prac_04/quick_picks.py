# How many quick picks? 5
#  1 12 14 15 30 36
#  2  5  8 33 38 41
#  2 12 19 22 29 43
# 13 21 28 29 42 43
#  3  4 10 11 32 44

import random

NUMBER_QUICK_PICKS = 5
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    """
    Main function to start the program.
    """
    number_of_picks = int(input("How many quick picks? "))
    display_quick_picks(number_of_picks)


def generate_quick_picks():
    """
    Generate a single quick pick of 6 unique random numbers between 1 and 45, sorted in ascending order.
    """
    numbers = sorted(random.sample(range(MINIMUM_NUMBER, MAXIMUM_NUMBER + 1), NUMBERS_PER_PICK))
    return numbers


def display_quick_picks(num_picks):
    """
    Display the requested number of quick picks, each containing 6 unique random numbers.
    """
    print(f"How many quick picks? {num_picks}")
    for _ in range(num_picks):
        quick_pick = generate_quick_picks()
        print(" ".join(f"{num:2d}" for num in quick_pick))


main()
