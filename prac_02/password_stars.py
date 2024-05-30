"""Password Stars program refactored to incorporate usage of functions"""

PASSWORD_LENGTH = 8


def main():
    """Main function to call the two functions get_password and print_password_asterisks"""
    password = get_password()
    print_password_asterisks(password)


def get_password():
    """get_password function used to get input from users"""
    password = input("Enter your password: ")
    while len(password) < PASSWORD_LENGTH:
        print(f"Password should be at least {PASSWORD_LENGTH} characters long.")
        password = input("Enter your password: ")
    return password


def print_password_asterisks(password):
    """print_password_asterisks prints the length of the password in asterisks"""
    print("*" * len(password))


# Call the main function
main()
