from functools import reduce

# map()

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print("Squares:", squares)

# filter()

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)

# reduce()

total = reduce(lambda a, b: a + b, numbers)

print("Sum:", total)
