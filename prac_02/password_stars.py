LENGTH_OF_PASSWORD = 8


def main():
    password = get_password()
    print_password_asterisks(password)


def get_password():
    password = input("Enter your password: ")
    while len(password) < LENGTH_OF_PASSWORD:
        print(f"Password should be at least {LENGTH_OF_PASSWORD} characters long.")
        password = input("Enter your password: ")
    return password


def print_password_asterisks(password):
    print("*" * len(password))


# Call the main function
main()l

