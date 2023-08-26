from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []  # created list to store list of

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:,.2f} added.\n")

        name = input("Name: ")

    print("\nThese are my guitars:")

    # Loop through the list of guitars and print their details
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == '__main__':
    main()
