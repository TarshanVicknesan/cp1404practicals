import csv
from collections import namedtuple
from prac_07.programming_language import ProgrammingLanguage


def main():
    languages = []
    with open('languages.csv', 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            reflection = parts[2] == "Yes"
            language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]))
            languages.append(language)
    for language in languages:
        print(language)


main()


def using_csv():
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
    in_file.close()


# using_csv()

def using_namedtuple():
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()
    Language = namedtuple('Language', 'name, typing, reflection, pointer_arithmetic, year')
    reader = csv.reader(in_file)
    for row in reader:
        language = Language._make(row)
        print(repr(language))
    in_file.close()


# using_namedtuple()

def using_csv_namedtuple():
    Language = namedtuple('Language', 'name, typing, reflection, pointer_arithmetic, year')
    in_file = open("languages.csv", "r")
    in_file.readline()
    for language in map(Language._make, csv.reader(in_file)):
        print(language.name, 'was released in', language.year)
        print(repr(language))

# using_csv_namedtuple()
