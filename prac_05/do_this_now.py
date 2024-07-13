# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
# name_width = max(len(pair[0]) for pair in data)
# score_width = max(len(str(pair[1])) for pair in data)
#
# for pair in data:
#     name, score = pair
#     print(f"{name:{name_width}} = {score:{score_width}}")
# print()

# data = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}
#
# name_width = max(len(name) for name in data.keys())
# score_width = max(len(str(score)) for score in data.values())
#
# for name, score in data.items():
#     print(f"{name:{name_width}} = {score:{score_width}}")
# print()

# write a function that takes a list of strings and returns a dictionary of pairs:
#
# string: length of string

# language: ["Python", "Java", "Scom"]


# languages = ["Python", "Java", "Scom"]
#
#
# def strings_to_length_dict(strings):
#     length_dictionary = {}
#     for string in strings:
#         length_dictionary[string] = len(string)
#     return length_dictionary
#
#
# length_dictionary = strings_to_length_dict(languages)
# print(length_dictionary)

import csv
from operator import itemgetter


def main():
    filename = 'countries.csv'

    country_data = []

    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for fields in reader:
            country = fields[0]
            capital = fields[1]
            population_str = fields[2].replace(',', '')
            population = int(population_str) if population_str.isdigit() else 0
            percent_of_country = float(fields[3].rstrip('%')) if fields[3].strip() else 0.0

            country_data.append({
                'Country': country,
                'Capital': capital,
                'Population': population,
                '% of country': percent_of_country
            })

    sorted_country_data = sorted(country_data, key=itemgetter('Country'))

    for data in sorted_country_data:
        print(f"{data['Country']:<30} - {data['Capital']:<20} - {data['Population']:,} ({data['% of country']}%)")


main()
