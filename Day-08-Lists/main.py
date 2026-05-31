# Creating a List

fruits = ["Apple", "Banana", "Mango"]

print("Original List:", fruits)

# Accessing Elements

print("First Fruit:", fruits[0])
print("Second Fruit:", fruits[1])

# Adding Elements

fruits.append("Orange")
print("After Append:", fruits)

# Removing Elements

fruits.remove("Banana")
print("After Remove:", fruits)

# List Length

print("Length:", len(fruits))

# Loop Through List

for fruit in fruits:
    print(fruit)
