# Day 7 - Strings 🐍

## 📌 Topics Covered
- Introduction to Strings
- String Indexing
- String Slicing
- String Methods
- String Operations

---

## 📖 What is a String?

A string is a sequence of characters enclosed in single quotes (' ') or double quotes (" ").

Example:

```python
name = "Python"
```

---

## 📖 Accessing Characters (Indexing)

Each character in a string has an index.

```python
text = "Python"

print(text[0])   # P
print(text[1])   # y
```

---

## 📖 String Slicing

Slicing is used to extract a portion of a string.

Syntax:

```python
string[start:end]
```

Example:

```python
text = "Python"

print(text[0:3])   # Pyt
print(text[2:6])   # thon
```

---

## 📖 Common String Methods

| Method | Description |
|----------|-------------|
| upper() | Converts to uppercase |
| lower() | Converts to lowercase |
| strip() | Removes extra spaces |
| replace() | Replaces text |
| split() | Splits string into list |
| find() | Finds character position |

Example:

```python
name = "python"

print(name.upper())
print(name.capitalize())
```

---

## 📖 String Concatenation

Joining strings together.

```python
first = "Hello"
second = "World"

print(first + " " + second)
```

Output:

```text
Hello World
```

---

## 📚 Key Points

- Strings store text data.
- Indexing starts from 0.
- Slicing extracts parts of strings.
- String methods simplify text processing.
- Strings are immutable.

---

## 🎯 Day 7 Completed

Strings are one of the most frequently used data types in Python.
