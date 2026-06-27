# Day 23 - Map, Filter & Reduce 🐍

## 📌 Topics Covered
- Introduction to `map()`
- Introduction to `filter()`
- Introduction to `reduce()`
- Lambda with map, filter & reduce
- Practical Examples

---

## 📖 What is `map()`?

`map()` applies a function to every item in an iterable and returns a new iterator.

Syntax:

```python
map(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)
```

Output:

```text
[1, 4, 9, 16]
```

---

## 📖 What is `filter()`?

`filter()` selects elements that satisfy a condition.

Syntax:

```python
filter(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)
```

Output:

```text
[2, 4, 6]
```

---

## 📖 What is `reduce()`?

`reduce()` repeatedly applies a function to reduce a sequence to a single value.

It is available in the `functools` module.

```python
from functools import reduce
```

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, numbers)

print(total)
```

Output:

```text
10
```

---

## 📖 Comparison

| Function | Purpose |
|----------|---------|
| map() | Transform every element |
| filter() | Select elements based on condition |
| reduce() | Reduce elements to a single value |

---

## 📚 Key Points

- `map()` transforms data.
- `filter()` filters data.
- `reduce()` combines data into one value.
- Lambda functions are commonly used with all three.

---

## 🎯 Day 23 Completed

`map()`, `filter()`, and `reduce()` are powerful functional programming tools in Python.
