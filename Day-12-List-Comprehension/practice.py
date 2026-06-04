# Practice Question 1

numbers = [x for x in range(1, 11)]

print(numbers)

# Practice Question 2

cubes = [x**3 for x in range(1, 6)]

print(cubes)

# Practice Question 3

odd_numbers = [x for x in range(1, 21) if x % 2 != 0]

print(odd_numbers)

# Practice Question 4

names = ["sam", "john", "alex"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)

# Mini Task

marks = [85, 90, 76, 65, 95]

passed = [mark for mark in marks if mark >= 75]

print("Passed Students Marks:", passed)
