CSV_FILENAME = "wimbledon.csv"
COUNTRY_COLUMN = 1
CHAMPION_COLUMN = 2


# Main function
def main():
    records = read_csv_records(CSV_FILENAME)
    champion_counts, countries = process_records(records)
    display_results(champion_counts, countries)


# Process records function
def process_records(records):
    champion_counts = {}
    unique_countries = set()

    for record in records:
        unique_countries.add(record[COUNTRY_COLUMN])
        if record[CHAMPION_COLUMN] in champion_counts:
            champion_counts[record[CHAMPION_COLUMN]] += 1
        else:
            champion_counts[record[CHAMPION_COLUMN]] = 1

    return champion_counts, unique_countries


# Display results function
def display_results(champion_counts, countries):
    print("Wimbledon Champions:")
    for champion, count in champion_counts.items():
        print(f"{champion}: {count} wins")

    countries_string = ", ".join(sorted(countries))
    print("\nCountries of champions in alphabetical order:")
    print(countries_string)


# Read CSV records function
def read_csv_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as csv_file:
        next(csv_file)  # Skip header line
        for line in csv_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


# Call the main function
main()



