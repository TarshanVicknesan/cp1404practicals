LENGTH_OF_PASSWORD = 8

password = input("Enter your password: ")
while len(password) < LENGTH_OF_PASSWORD:
    print(f"Password should at least be {LENGTH_OF_PASSWORD} characters long.")
    password = input("Enter your password: ")

print("*" * len(password))
