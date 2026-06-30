import json

# Practice Question 1

employee = {
    "name": "John",
    "salary": 50000,
    "department": "IT"
}

json_employee = json.dumps(employee, indent=4)

print(json_employee)

# Practice Question 2

data = '{"city":"Pune","state":"Maharashtra"}'

location = json.loads(data)

print(location["city"])

# Practice Question 3

book = {
    "title": "Python Basics",
    "price": 499
}

with open("book.json", "w") as file:
    json.dump(book, file, indent=4)

print("Book data saved.")

# Practice Question 4

with open("book.json", "r") as file:
    book_data = json.load(file)

print(book_data)

# Mini Task

student = {
    "name": "Sam",
    "marks": 95,
    "course": "Python"
}

student_json = json.dumps(student, indent=4)

print(student_json)
