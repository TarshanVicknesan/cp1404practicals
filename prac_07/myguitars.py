import csv
from prac_07.guitar import Guitar


def read_guitars_from_csv(filename):
    """Read the CSV file and create a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(row) == 3:
                name, year, cost = row
                year = int(year)
                cost = float(cost)
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
    return guitars


def display_guitars(guitars, title):
    """Display the list of guitars."""
    print(title)
    for guitar in guitars:
        print(guitar)


def main():
    """Main function to read, display, sort, and display guitars."""
    guitars = read_guitars_from_csv('guitars.csv')

    # Display the unsorted list of guitars
    display_guitars(guitars, "Guitars (Unsorted):")

    # Sort the list of guitars by year
    guitars.sort()

    # Display the sorted list of guitars
    display_guitars(guitars, "\nGuitars (Sorted by Year - Oldest to Newest):")


# Define the __lt__ (less than) method in the Guitar class to compare by year
def guitar_lt(self, other):
    return self.year < other.year


setattr(Guitar, "__lt__", guitar_lt)

if __name__ == '__main__':
    main()
