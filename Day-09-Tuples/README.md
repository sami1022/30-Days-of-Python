# Day 9 - Tuples 🐍

## 📌 Topics Covered
- Introduction to Tuples
- Creating Tuples
- Accessing Tuple Elements
- Tuple Slicing
- Tuple Methods
- Differences Between Lists and Tuples

---

## 📖 What is a Tuple?

A tuple is a collection of items stored in a single variable.

Example:

```python
fruits = ("Apple", "Banana", "Mango")
```

Tuples are:
- Ordered
- Immutable (cannot be changed)
- Allow duplicate values

---

## 📖 Creating a Tuple

```python
numbers = (10, 20, 30, 40)
print(numbers)
```

---

## 📖 Accessing Tuple Elements

Indexing starts from 0.

```python
colors = ("Red", "Green", "Blue")

print(colors[0])
print(colors[1])
```

Output:

```text
Red
Green
```

---

## 📖 Tuple Slicing

Extract a portion of a tuple.

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

Output:

```text
(20, 30, 40)
```

---

## 📖 Tuple Methods

| Method | Description |
|----------|-------------|
| count() | Counts occurrences |
| index() | Finds position of value |

Example:

```python
numbers = (1, 2, 3, 2)

print(numbers.count(2))
print(numbers.index(3))
```

---

## 📖 List vs Tuple

| List | Tuple |
|--------|--------|
| Mutable | Immutable |
| Uses [] | Uses () |
| More flexible | Faster |

---

## 📚 Key Points

- Tuples are immutable.
- Tuples use parentheses `()`.
- Tuples can store different data types.
- Useful when data should not change.

---

## 🎯 Day 9 Completed

Tuples are great for storing fixed collections of data.
