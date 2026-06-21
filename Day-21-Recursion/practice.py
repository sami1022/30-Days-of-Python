# Practice Question 1

def print_numbers(n):

    if n == 0:
        return

    print_numbers(n - 1)

    print(n)

print_numbers(5)

# Practice Question 2

def sum_numbers(n):

    if n == 1:
        return 1

    return n + sum_numbers(n - 1)

print("Sum:", sum_numbers(5))

# Practice Question 3

def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

print("Power:", power(2, 3))

# Mini Task

def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci Series:")

for i in range(8):
    print(fibonacci(i), end=" ")
