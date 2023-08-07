def main():
    user_data = {}
    email = input("Email: ").strip()

    while email != "":
        name = extract_name(email)
        is_correct = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if is_correct != "y" and is_correct != "":
            name = input("Name: ").strip().title()

        user_data[email] = name
        email = input("Email: ").strip()

    print("\nName and Email pairs:")
    for email, name in user_data.items():
        print(f"{name} ({email})")


def extract_name(email):
    name = email.split('@')[0]
    name = ''.join(c for c in name if c.isalpha() or c.isspace())
    name = name.title()
    return name


main()



