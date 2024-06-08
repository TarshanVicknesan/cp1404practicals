"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

# Constants
MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters:", SPECIAL_CHARACTERS)

    while True:
        password = input("> ")
        if is_valid_password(password):
            print(f"Your {len(password)} character password is valid: {password}")
            break
        else:
            print("Invalid password!")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # Check the length of the password
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    # Initialize counters for different types of characters
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    # Count the occurrences of each type of character in the password
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif SPECIAL_CHARS_REQUIRED and char in SPECIAL_CHARACTERS:
            count_special += 1

    # Check if all required character types are present
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    if SPECIAL_CHARS_REQUIRED and count_special == 0:
        return False

    return True


main()
