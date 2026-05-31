# Day 8 - Lists 🐍

## 📌 Topics Covered
- Introduction to Lists
- Creating Lists
- Accessing Elements
- List Slicing
- List Methods
- Looping Through Lists

---

## 📖 What is a List?

A list is a collection of multiple items stored in a single variable.

Example:

```python
fruits = ["Apple", "Banana", "Mango"]
```

Lists are:
- Ordered
- Mutable (can be changed)
- Allow duplicate values

---

## 📖 Accessing List Elements

Lists use indexing starting from 0.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
```

Output:

```text
Apple
Banana
```

---

## 📖 List Slicing

Extract a portion of a list.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

---

## 📖 Common List Methods

| Method | Description |
|----------|-------------|
| append() | Add an item |
| insert() | Insert at position |
| remove() | Remove item |
| pop() | Remove by index |
| sort() | Sort list |
| reverse() | Reverse list |
| len() | Find length |

Example:

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)
```

---

## 📖 Looping Through a List

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

---

## 📚 Key Points

- Lists store multiple values.
- Lists are mutable.
- Indexing starts from 0.
- Many built-in methods simplify list operations.

---

## 🎯 Day 8 Completed

Lists are one of the most important data structures in Python.
