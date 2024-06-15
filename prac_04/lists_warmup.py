numbers = [3, 1, 4, 1, 5, 9, 2]

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all the elements from numbers except the first two (slice)
print(numbers[2:])  # [4, 1, 5, 9, 1]

# Print whether 9 is an element of numbers
print(9 in numbers)  # True

print(numbers[0])  # "ten"
print(numbers[-1])  # 1
print(numbers[3])  # 1
print(numbers[:-1])  # ["ten", 1, 4, 1, 5, 9]
print(numbers[3:4])  # [1]
print(5 in numbers)  # True
print(7 in numbers)  # False
print("3" in numbers)  # False
print(numbers + [6, 5, 3])  # ["ten", 1, 4, 1, 5, 9, 1, 6, 5, 3]
