# Practice Question 1

fruits = ["Apple", "Banana", "Mango"]

fruit_iterator = iter(fruits)

print(next(fruit_iterator))
print(next(fruit_iterator))
print(next(fruit_iterator))

# Practice Question 2

def even_numbers(limit):

    for i in range(2, limit + 1, 2):
        yield i

print("\nEven Numbers:")

for number in even_numbers(10):
    print(number)

# Practice Question 3

cube_generator = (x ** 3 for x in range(1, 6))

print("\nCube Values:")

for cube in cube_generator:
    print(cube)

# Practice Question 4

def greetings():

    yield "Hello"
    yield "Welcome"
    yield "Goodbye"

print("\nGreetings:")

for message in greetings():
    print(message)

# Mini Task

def fibonacci(limit):

    a, b = 0, 1

    for _ in range(limit):
        yield a
        a, b = b, a + b

print("\nFibonacci Series:")

for num in fibonacci(10):
    print(num)
