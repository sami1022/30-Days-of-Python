# Day 24 - Iterators and Generators 🐍

## 📌 Topics Covered
- Introduction to Iterators
- Using `iter()` and `next()`
- Introduction to Generators
- `yield` Keyword
- Generator Expressions
- Iterators vs Generators

---

## 📖 What is an Iterator?

An iterator is an object that allows you to traverse through all elements of a collection one at a time.

Python provides two built-in functions:

- `iter()` → Creates an iterator.
- `next()` → Returns the next element.

Example:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
10
20
30
```

---

## 📖 What is a Generator?

A generator is a special type of function that returns values one at a time using the `yield` keyword.

Unlike `return`, `yield` pauses the function and remembers its state.

Example:

```python
def count():

    yield 1
    yield 2
    yield 3

for number in count():
    print(number)
```

Output:

```text
1
2
3
```

---

## 📖 Generator Expression

A generator expression looks similar to list comprehension but uses parentheses `()`.

Example:

```python
numbers = (x * x for x in range(5))

for num in numbers:
    print(num)
```

Output:

```text
0
1
4
9
16
```

---

## 📖 Iterator vs Generator

| Iterator | Generator |
|----------|-----------|
| Uses `iter()` | Uses `yield` |
| More memory | Memory Efficient |
| Manual iteration | Automatic iteration |
| Can be complex | Easier to create |

---

## 📚 Key Points

- Iterators help traverse collections.
- `next()` retrieves the next element.
- Generators use the `yield` keyword.
- Generators are memory efficient.
- Generator expressions are similar to list comprehensions.

---

## 🎯 Day 24 Completed

Iterators and Generators are powerful tools for handling large datasets efficiently and are commonly used in Python applications.
