# Creating a Dictionary

student = {
    "name": "Sam",
    "age": 20,
    "course": "Python"
}

print("Student Details:")
print(student)

# Accessing Values

print("Name:", student["name"])
print("Age:", student["age"])

# Adding New Key

student["city"] = "Pune"

# Updating Value

student["age"] = 21

print("\nUpdated Dictionary:")
print(student)

# Dictionary Methods

print("\nKeys:", student.keys())
print("Values:", student.values())

# Loop Through Dictionary

for key, value in student.items():
    print(key, ":", value)
