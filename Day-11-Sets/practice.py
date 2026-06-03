# Practice Question 1

numbers = {10, 20, 30, 40, 50}

print(numbers)

# Practice Question 2

numbers.add(60)

print(numbers)

# Practice Question 3

numbers.remove(20)

print(numbers)

# Practice Question 4

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a.union(b))
print("Intersection:", a.intersection(b))

# Mini Task

students = {"Sam", "John", "Alex"}

students.add("David")

print("\nStudent Set:")

for student in students:
    print(student)

print("Total Unique Students:", len(students))
