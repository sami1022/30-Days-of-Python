# Basic Exception Handling

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Please enter a valid integer.")

# Division Example

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program Finished.")
