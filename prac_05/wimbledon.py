COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Read Wimbledon data from a CSV file and display champion counts and countries.
    """

    filename = "wimbledon.csv"
    records = read_records(filename)
    champions_count, countries_set = filters_records(records)
    display_results(champions_count, countries_set)


def filters_records(records):
    """Count Wimbledon champions and identify unique winning countries.
    """

    champions_count = {}
    countries_set = set()

    for record in records:
        countries_set.add(record[COUNTRY_INDEX])
        champion_name = record[CHAMPION_INDEX]
        champions_count[champion_name] = champions_count.get(champion_name, 0) + 1

    return champions_count, countries_set


def display_results(champions_count, countries_set):
    """Display Wimbledon champion counts and list of winning countries.
    """

    print("Wimbledon Champions:")
    for name, count in champions_count.items():
        print(f"{name}: {count}")

    countries_list = sorted(countries_set)
    print(f"\n{len(countries_list)} countries have won Wimbledon:")
    print(", ".join(countries_list))


def read_records(filename):
    """Read Wimbledon data from a CSV file.
    """

    records = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split(",")
            records.append(parts)

    return records


main()
