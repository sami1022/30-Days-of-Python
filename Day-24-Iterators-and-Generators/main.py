# Iterator Example

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Generator Example

def countdown(n):

    while n > 0:
        yield n
        n -= 1

print("\nCountdown:")

for number in countdown(5):
    print(number)

# Generator Expression

squares = (x ** 2 for x in range(1, 6))

print("\nSquares:")

for square in squares:
    print(square)
