# Practice Questions

# 1. Print numbers from 1 to 10

for i in range(1, 11):
    print(i)

# 2. Print even numbers from 1 to 20

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 3. Multiplication Table

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 4. Sum of First 10 Numbers

total = 0

for i in range(1, 11):
    total += i

print("Sum:", total)

# Mini Task

password = "python"

user_input = input("Enter password: ")

while user_input != password:
    user_input = input("Wrong password. Try again: ")

print("Access Granted")
