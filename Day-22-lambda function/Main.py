# Basic Lambda Function

square = lambda x: x * x

print("Square:", square(5))

# Lambda with Multiple Arguments

add = lambda a, b: a + b

print("Addition:", add(10, 20))

# Lambda for Even/Odd

even = lambda num: num % 2 == 0

print("Is Even:", even(8))

# Lambda with sorted()

students = [
    ("Sam", 90),
    ("John", 75),
    ("Alex", 85)
]

students.sort(key=lambda x: x[1])

print("Sorted List:", students)
