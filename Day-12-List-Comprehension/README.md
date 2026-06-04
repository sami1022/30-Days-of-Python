# Day 12 - List Comprehension 🐍

## 📌 Topics Covered
- Introduction to List Comprehension
- Syntax
- Using Conditions
- Creating Lists Efficiently
- Comparison with Traditional Loops

---

## 📖 What is List Comprehension?

List Comprehension provides a concise way to create lists in Python.

Instead of using multiple lines with loops, we can create lists in a single line.

Traditional Method:

```python
numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)
```

Using List Comprehension:

```python
numbers = [i for i in range(1, 6)]

print(numbers)
```

Output:

```text
[1, 2, 3, 4, 5]
```

---

## 📖 Syntax

```python
new_list = [expression for item in iterable]
```

Example:

```python
squares = [x**2 for x in range(1, 6)]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

## 📖 Using Conditions

```python
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

print(even_numbers)
```

Output:

```text
[2, 4, 6, 8, 10]
```

---

## 📖 String Example

```python
word = "Python"

letters = [char for char in word]

print(letters)
```

Output:

```text
['P', 'y', 't', 'h', 'o', 'n']
```

---

## 📚 Key Points

- List comprehensions make code shorter and cleaner.
- They are often faster than traditional loops.
- Conditions can be added easily.
- Useful for transforming and filtering data.

---

## 🎯 Day 12 Completed

List comprehensions are one of the most powerful and commonly used Python features.
