# Writing to a File

with open("sample.txt", "w") as file:
    file.write("Welcome to Python File Handling")

print("Data written successfully!")

# Reading from File

with open("sample.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)

# Appending Data

with open("sample.txt", "a") as file:
    file.write("\nLearning Python is fun!")

print("\nData appended successfully!")
