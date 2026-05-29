# Practice Questions

# 1. Create a function to print your name

def my_name():
    print("Sam")

my_name()

# 2. Create a function to add two numbers

def addition(a, b):
    return a + b

print("Addition:", addition(5, 10))

# 3. Create a function to find the largest number

def largest(a, b):
    if a > b:
        return a
    return b

print("Largest:", largest(20, 15))

# 4. Create a function to check even or odd

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"

print(check_even_odd(7))

# Mini Task

def student_info(name, course):
    print("Name:", name)
    print("Course:", course)

student_info("Sam", "Python")
