# Basic List Comprehension

numbers = [x for x in range(1, 11)]

print("Numbers:", numbers)

# Squares

squares = [x**2 for x in range(1, 6)]

print("Squares:", squares)

# Even Numbers

evens = [x for x in range(1, 21) if x % 2 == 0]

print("Even Numbers:", evens)

# Convert String to List

word = "Python"

letters = [char for char in word]

print("Letters:", letters)
