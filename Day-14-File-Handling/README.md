# Day 14 - File Handling 

## 📌 Topics Covered
- Introduction to File Handling
- Opening Files
- Reading Files
- Writing Files
- Appending Data
- Closing Files
- Using `with` Statement

---

## 📖 What is File Handling?

File handling allows Python programs to:
- Read data from files
- Write data to files
- Store information permanently

Python provides built-in functions to work with files.

---

## 📖 Opening a File

Syntax:

```python
file = open("sample.txt", "r")
```

Modes:

| Mode | Description |
|--------|------------|
| r | Read |
| w | Write |
| a | Append |
| x | Create |
| rb | Read Binary |
| wb | Write Binary |

---

## 📖 Reading a File

```python
file = open("sample.txt", "r")

print(file.read())

file.close()
```

---

## 📖 Writing to a File

```python
file = open("sample.txt", "w")

file.write("Hello Python")

file.close()
```

---

## 📖 Appending Data

```python
file = open("sample.txt", "a")

file.write("\nNew Line Added")

file.close()
```

---

## 📖 Using `with` Statement

Recommended method:

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

Benefits:
- Automatically closes the file
- Cleaner code
- Safer resource management

---

## 📚 Key Points

- Files store data permanently.
- Always close files after use.
- `with` statement is preferred.
- Different modes perform different operations.

---

## 🎯 Day 14 Completed

File handling is essential for storing and retrieving data in real-world applications.
