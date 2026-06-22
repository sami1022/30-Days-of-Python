# Practice Question 1

cube = lambda x: x ** 3

print("Cube:", cube(3))

# Practice Question 2

multiply = lambda a, b: a * b

print("Multiplication:", multiply(5, 4))

# Practice Question 3

largest = lambda a, b: a if a > b else b

print("Largest:", largest(20, 15))

# Practice Question 4

names = ["sam", "john", "alex"]

uppercase_names = list(map(lambda name: name.upper(), names))

print(uppercase_names)

# Mini Task

numbers = [10, 20, 30, 40, 50]

doubled = list(map(lambda x: x * 2, numbers))

print("Doubled Numbers:", doubled)
