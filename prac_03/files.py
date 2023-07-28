# # Task 1: Write the user's name to "name.txt"
# name = input("Enter your name: ")
# file = open("name.txt", "w")
# file.write(name)
# file.close()

# # Task 2: Read the name from "name.txt" and print it
# file = open("name.txt", "r")
# name = file.read()
# file.close()
# print(f"Your name is {name}")

# # Task 3: Read the first two numbers from "numbers.txt" and add them
# file = open("numbers.txt", "r")
# numbers = file.readlines()
# file.close()
# first_number = int(numbers[0])
# second_number = int(numbers[1])
# result = first_number + second_number
# print(f"The sum of the first two numbers is {result}")
#
# Task 4: Print the total for all lines in a file with any number of numbers
filename = "numbers.txt"
total = 0
file = open(filename, "r")
numbers = file.readlines()
file.close()
for number in numbers:
    total += int(number)
print(f"The total sum is {total}")

