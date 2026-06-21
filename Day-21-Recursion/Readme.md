# Day 21 - Recursion 🐍

## 📌 Topics Covered
- Introduction to Recursion
- Recursive Functions
- Base Case
- Recursive Case
- Factorial Using Recursion

---

## 📖 What is Recursion?

Recursion is a programming technique where a function calls itself to solve a problem.

A recursive function must have:
1. Base Case (stopping condition)
2. Recursive Case (function calling itself)

---

## 📖 Why Use Recursion?

Recursion is useful for:
- Tree Traversal
- Graph Algorithms
- Divide and Conquer Problems
- Mathematical Calculations

---

## 📖 Basic Example

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)

countdown(5)
```

Output:

```text
5
4
3
2
1
```

---

## 📖 Factorial Using Recursion

Mathematical Formula:

n! = n × (n - 1)!

Example:

```python
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

---

## 📖 Understanding Base Case

Without a base case:

```python
def demo():
    demo()
```

The function will run forever and cause a RecursionError.

Always define a stopping condition.

---

## 📚 Key Points

- Recursion means a function calls itself.
- Every recursive function needs a base case.
- Recursive problems are often simpler to write.
- Incorrect recursion may cause infinite calls.

---

## 🎯 Day 21 Completed

Recursion is a powerful concept that appears frequently in coding interviews and advanced algorithms.
