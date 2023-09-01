import csv
from guitar import Guitar

# Read the CSV file and create a list of Guitar objects
guitars = []
with open('guitars.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if len(row) == 3:
            name, year, cost = row
            year = int(year)
            cost = float(cost)
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)

# Display the unsorted list of guitars
print("Guitars (Unsorted):")
for guitar in guitars:
    print(guitar)


# Define the __lt__ (less than) method in the Guitar class to compare by year
def guitar_lt(self, other):
    return self.year < other.year


setattr(Guitar, "__lt__", guitar_lt)

# Sort the list of guitars by year
guitars.sort()

# Display the sorted list of guitars
print("\nGuitars (Sorted by Year - Oldest to Newest):")
for guitar in guitars:
    print(guitar)
