# Practice Questions

# 1. Positive or Negative Number
num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
else:
    print("Negative Number")

# 2. Largest Number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)

# 3. Password Checker
password = input("Enter password: ")

if password == "python123":
    print("Access Granted")
else:
    print("Wrong Password")

# Mini Task
temperature = int(input("Enter temperature: "))

if temperature > 30:
    print("Hot Weather")
else:
    print("Cool Weather")
