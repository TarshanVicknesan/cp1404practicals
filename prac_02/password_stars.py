LENGTH_OF_PASSWORD = 8


def main():
    password = input("Enter your password: ")
    while len(password) < LENGTH_OF_PASSWORD:
        print(f"Password should be at least {LENGTH_OF_PASSWORD} characters long.")
        password = input("Enter your password: ")

    print("*" * len(password))


# Call the main function


main()
