# Practice Question 1

try:
    age = int(input("Enter your age: "))
    print("Age:", age)
except ValueError:
    print("Invalid age entered.")

# Practice Question 2

try:
    number = int(input("Enter a number: "))
    print("Square:", number * number)
except ValueError:
    print("Only integers are allowed.")

# Practice Question 3

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Division:", num1 / num2)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Invalid input.")

# Mini Task

try:
    marks = int(input("Enter marks: "))

    if marks < 0:
        raise ValueError("Marks cannot be negative.")

    print("Marks:", marks)

except ValueError as e:
    print(e)
