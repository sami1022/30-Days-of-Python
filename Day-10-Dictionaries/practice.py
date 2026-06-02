# Practice Question 1

employee = {
    "name": "John",
    "salary": 50000
}

print(employee)

# Practice Question 2

print(employee["name"])

# Practice Question 3

employee["department"] = "IT"

print(employee)

# Practice Question 4

for key, value in employee.items():
    print(key, ":", value)

# Mini Task

book = {
    "title": "Python Basics",
    "author": "ABC",
    "price": 499
}

print("\nBook Details")

for key, value in book.items():
    print(key, ":", value)
