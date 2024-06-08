import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# print(random.randint(5, 20)), this code line indicates that it will print a random number between 5 and 20
# What was the smallest number you could have seen, what was the largest?
# the smallest number would be 5, and the biggest number would be 20.

# What did you see on line 2?
# print(random.randrange(3, 10, 2)), this line prints a number between 3 and 10, but with an increment of 2.
# What was the smallest number you could have seen, what was the largest?
# the smallest number that could've been produced is 3 and the biggest would have been 9.
# Could line 2 have produced a 4?
# No it couldn't, cause since the starting number is 3 the next number would have been 5 because of the step up 2.


# What did you see on line 3?
# print(random.uniform(2.5, 5.5)) This line will print a random decimal/float number between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# The smallest number would be 2.5 and the biggest would be 5.5.
