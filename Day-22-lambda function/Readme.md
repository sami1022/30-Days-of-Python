# Day 22 - Lambda Functions 🐍

## 📌 Topics Covered
- Introduction to Lambda Functions
- Syntax of Lambda Functions
- Lambda with Multiple Arguments
- Using Lambda with sorted()
- Advantages of Lambda Functions

---

## 📖 What is a Lambda Function?

A lambda function is a small anonymous function that can have any number of arguments but only one expression.

Syntax:

```python
lambda arguments : expression
```

Example:

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

---

## 📖 Why Use Lambda Functions?

Lambda functions are useful when:
- A function is needed only once.
- Short and simple operations are required.
- Used with functions like `map()`, `filter()`, and `sorted()`.

---

## 📖 Lambda with Multiple Arguments

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output:

```text
30
```

---

## 📖 Lambda with sorted()

```python
students = [
    ("Sam", 90),
    ("John", 75),
    ("Alex", 85)
]

students.sort(key=lambda x: x[1])

print(students)
```

Output:

```text
[('John', 75), ('Alex', 85), ('Sam', 90)]
```

---

## 📚 Key Points

- Lambda functions are anonymous functions.
- Defined using the `lambda` keyword.
- Useful for short operations.
- Often used with `map()`, `filter()`, and `sorted()`.

---

## 🎯 Day 22 Completed

Lambda functions help write concise and readable Python code.
