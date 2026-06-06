# Practice Question 1

with open("student.txt", "w") as file:
    file.write("Name: Sam\n")
    file.write("Course: Python\n")

print("Student data saved.")

# Practice Question 2

with open("student.txt", "r") as file:
    print(file.read())

# Practice Question 3

with open("student.txt", "a") as file:
    file.write("Age: 20\n")

print("New data added.")

# Practice Question 4

with open("student.txt", "r") as file:
    content = file.read()

print(content)

# Mini Task

with open("notes.txt", "w") as file:
    file.write("Day 14 - File Handling Completed")

print("Notes saved successfully!")
