# Task 1: Write code that asks the user for their name,
# then opens a file called name.txt and writes that name to it. Use open and close for this question.
# name = input("Please enter your name: ")
# file = open("name.txt", "w")
# file.write(name)
# file.close()

# Task 2: In the same file, but as if it were a separate program,
# write code that opens "name.txt" and reads the name (as above) then prints (note the exact output)
# file = open("name.txt", "r")
# name = file.read().strip()
# file.close()
# print(f"Your name is {name}")

# Task 3: Write code that opens numbers.txt, reads only the first two numbers,
# adds them together then prints the result,
# which should be... 59. Use with instead of open and close for this question.
# with open("numbers.txt", "r") as file:
#     first_number = int(file.readline())
#     second_number = int(file.readline())
# result = first_number + second_number
# print(result)

# Task 4: Now write a fourth block of code that prints the total for all lines in numbers.txt.
# This should work for a file with any number of numbers.
# Use with instead of open and close for this question.
# total = 0
# with open("numbers.txt", "r") as file:
#     for line in file:
#         total += int(line)
# print(total)

