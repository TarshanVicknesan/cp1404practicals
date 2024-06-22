def main():
    users = {}
    email = input("Email: ").strip()

    while email:
        name_from_email = extract_from_email(email)
        confirmation = input(f"Is your name {name_from_email}? (Y/n) ").strip().lower()

        if confirmation == "" or confirmation == "y":
            name = name_from_email
        else:
            name = input("Name: ").strip().title()

        users[email] = name
        email = input("Email: ").strip()

    print("\nUsers:")
    for email, name in users.items():
        print(f"{name} ({email})")


def extract_from_email(email):
    # Extract the name from the email address
    parts = email.split('@')[0].split('.')
    name = ' '.join(parts).title()
    return name


main()
