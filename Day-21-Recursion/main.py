# Countdown Using Recursion

def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)

countdown(5)

# Factorial Using Recursion

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print("Factorial:", factorial(5))
