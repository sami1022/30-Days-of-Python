import json

# Python Dictionary

student = {
    "name": "Sam",
    "age": 20,
    "course": "Python"
}

# Dictionary to JSON

json_data = json.dumps(student, indent=4)

print("JSON Data:")
print(json_data)

# JSON to Dictionary

python_data = json.loads(json_data)

print("\nStudent Name:", python_data["name"])

# Write JSON to File

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("\nData saved to student.json")

# Read JSON File

with open("student.json", "r") as file:
    data = json.load(file)

print("\nRead from File:")
print(data)
