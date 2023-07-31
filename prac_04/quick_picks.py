import random

# Constants
NUM_QUICK_PICKS = 5
MININUM_NUM = 1
MAXIMUM_NUM = 45
NUM_NUMBERS_PER_PICK = 6


def main():
    num_picks = int(input("How many quick picks? "))
    display_quick_picks(num_picks)


def generate_quick_pick():
    numbers = random.sample(range(MININUM_NUM, MAXIMUM_NUM + 1), NUM_NUMBERS_PER_PICK)
    numbers.sort()
    return numbers


def display_quick_picks(num_picks):
    print(f"How many quick picks? {num_picks}")
    for i in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2d}" for num in quick_pick))


main()
