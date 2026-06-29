import re

# Search Example

text = "Python Programming"

result = re.search("Python", text)

if result:
    print("Match Found")

# Find All Numbers

sentence = "Age: 20, Marks: 95"

numbers = re.findall(r"\d+", sentence)

print("Numbers:", numbers)

# Replace Text

message = "I love Java"

updated = re.sub("Java", "Python", message)

print(updated)

# Split String

fruits = "Apple,Banana,Mango"

print(re.split(",", fruits))
