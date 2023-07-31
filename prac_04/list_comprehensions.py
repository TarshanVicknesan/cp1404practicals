# Original data
names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']

# List comprehension to create a list of all the full_names in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

# List comprehension to create a list of integers from the almost_numbers list of strings
numbers = [int(number) for number in almost_numbers]
print(numbers)

# List comprehension to create a list of only the numbers that are greater than 9 from the numbers (not strings) you just created
numbers_greater_than_9 = [number for number in numbers if number > 9]
print(numbers_greater_than_9)

# (More advanced) Use a list comprehension and the join string method to create a string (not list) of the last names for those full_names longer than 11 characters
long_last_names = [name.split()[-1] for name in full_names if len(name) > 11]
result_string = ", ".join(long_last_names)
print(result_string)

# List comprehension to create a list of all the full_names in uppercase format
uppercase_full_names = [name.upper() for name in full_names]
print(uppercase_full_names)

# List comprehension to create a list of the squares of the numbers from the numbers list
squares = [number ** 2 for number in numbers]
print(squares)

# List comprehension to create a list of strings, where each string contains the first and last names joined with a space from the full_names list
first_and_last_names = [" ".join(name.split()[:2]) for name in full_names]
print(first_and_last_names)

# List comprehension to create a list of the lengths of each name in the names list
name_lengths = [len(name) for name in names]
print(name_lengths)

# List comprehension to create a list of only the names that have the letter 'a' (case insensitive) in the names list
names_with_a = [name for name in names if 'a' in name.lower()]
print(names_with_a)

# List comprehension to create a list of the reversed names from the names list
reversed_names = [name[::-1] for name in names]
print(reversed_names)
