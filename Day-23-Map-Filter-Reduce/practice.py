from functools import reduce

# Practice Question 1

numbers = [2, 4, 6, 8]

doubled = list(map(lambda x: x * 2, numbers))

print("Doubled:", doubled)

# Practice Question 2

numbers = [5, 10, 15, 20, 25]

greater_than_10 = list(filter(lambda x: x > 10, numbers))

print("Greater than 10:", greater_than_10)

# Practice Question 3

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda a, b: a * b, numbers)

print("Product:", product)

# Practice Question 4

names = ["sam", "john", "alex"]

capitalized = list(map(lambda x: x.capitalize(), names))

print("Capitalized:", capitalized)

# Mini Task

marks = [45, 72, 81, 39, 90]

passed = list(filter(lambda x: x >= 50, marks))

average = reduce(lambda a, b: a + b, passed) / len(passed)

print("Passed Marks:", passed)
print("Average:", average)
