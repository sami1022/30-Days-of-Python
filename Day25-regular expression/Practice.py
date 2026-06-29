import re

# Practice Question 1

text = "My phone number is 9876543210"

numbers = re.findall(r"\d+", text)

print(numbers)

# Practice Question 2

email = "student@gmail.com"

if re.search("@gmail\.com$", email):
    print("Valid Gmail Address")

# Practice Question 3

sentence = "Python is easy"

updated = re.sub("easy", "powerful", sentence)

print(updated)

# Practice Question 4

words = "Apple Orange Mango"

print(re.split(" ", words))

# Mini Task

password = "Python@123"

if re.search(r"\d", password):
    print("Password contains a digit")

if re.search(r"[A-Z]", password):
    print("Password contains an uppercase letter")

if re.search(r"[@#$%^&*!]", password):
    print("Password contains a special character")
