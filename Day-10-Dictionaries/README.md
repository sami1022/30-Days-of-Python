# Day 10 - Dictionaries 🐍

## 📌 Topics Covered
- Introduction to Dictionaries
- Creating Dictionaries
- Accessing Values
- Adding and Updating Items
- Dictionary Methods
- Looping Through Dictionaries

---

## 📖 What is a Dictionary?

A dictionary is a collection of data stored as **key-value pairs**.

Example:

```python
student = {
    "name": "Sam",
    "age": 20,
    "course": "Python"
}
```

Dictionaries are:
- Ordered (Python 3.7+)
- Mutable (can be changed)
- Do not allow duplicate keys

---

## 📖 Accessing Values

Use the key to access a value.

```python
student = {
    "name": "Sam",
    "age": 20
}

print(student["name"])
print(student["age"])
```

Output:

```text
Sam
20
```

---

## 📖 Adding and Updating Items

```python
student = {
    "name": "Sam"
}

student["age"] = 20
student["name"] = "John"

print(student)
```

---

## 📖 Common Dictionary Methods

| Method | Description |
|----------|-------------|
| keys() | Returns all keys |
| values() | Returns all values |
| items() | Returns key-value pairs |
| get() | Gets value safely |
| pop() | Removes item |
| update() | Updates dictionary |

Example:

```python
student = {
    "name": "Sam",
    "age": 20
}

print(student.keys())
print(student.values())
```

---

## 📖 Looping Through a Dictionary

```python
student = {
    "name": "Sam",
    "age": 20
}

for key, value in student.items():
    print(key, ":", value)
```

---

## 📚 Key Points

- Dictionaries store data as key-value pairs.
- Keys must be unique.
- Values can be of any data type.
- Dictionaries are mutable.

---

## 🎯 Day 10 Completed

Dictionaries are widely used for storing structured data in Python applications.
