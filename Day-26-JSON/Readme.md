# Day 26 - JSON 🐍

## 📌 Topics Covered
- Introduction to JSON
- JSON Data Types
- Converting Python Objects to JSON
- Converting JSON to Python Objects
- Reading JSON Files
- Writing JSON Files

---

## 📖 What is JSON?

**JSON (JavaScript Object Notation)** is a lightweight data-interchange format used to store and exchange data between applications.

It is:
- Human-readable
- Lightweight
- Language-independent
- Widely used in APIs and web applications

Python provides the built-in **`json`** module to work with JSON.

```python
import json
```

---

## 📖 Python Dictionary to JSON

Use `json.dumps()` to convert a Python object into a JSON string.

```python
import json

student = {
    "name": "Sam",
    "age": 20,
    "course": "Python"
}

json_data = json.dumps(student)

print(json_data)
```

Output:

```text
{"name": "Sam", "age": 20, "course": "Python"}
```

---

## 📖 JSON to Python Dictionary

Use `json.loads()` to convert a JSON string into a Python object.

```python
import json

data = '{"name":"Sam","age":20}'

student = json.loads(data)

print(student["name"])
```

Output:

```text
Sam
```

---

## 📖 Writing JSON to a File

```python
import json

student = {
    "name": "Sam",
    "age": 20
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

---

## 📖 Reading JSON from a File

```python
import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
```

---

## 📚 Key Points

- JSON is widely used for data exchange.
- `json.dumps()` converts Python objects to JSON strings.
- `json.loads()` converts JSON strings to Python objects.
- `json.dump()` writes JSON to a file.
- `json.load()` reads JSON from a file.

---

## 🎯 Day 26 Completed

JSON is one of the most important concepts for working with APIs, web development, and data exchange.
