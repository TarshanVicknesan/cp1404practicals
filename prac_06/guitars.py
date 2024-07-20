from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []

    name = input("Name: ").strip()

    while name:
        year = input("Year: ").strip()
        if not year.isdigit():
            print("Invalid year input. Please enter a valid year.")
            name = input("Name: ").strip()
            continue
        year = int(year)

        cost = input("Cost: $").strip()
        try:
            cost = float(cost)
        except ValueError:
            print("Invalid cost input. Please enter a valid number.")
            name = input("Name: ").strip()
            continue

        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.\n")

        name = input("Name: ").strip()

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost:,.2f}{vintage_string}")
    else:
        print("\nNo guitars added.")

main()
