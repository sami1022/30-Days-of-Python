# Day 13 - Modules 🐍

## 📌 Topics Covered
- Introduction to Modules
- Importing Modules
- Using Built-in Modules
- Import Specific Functions
- Creating Custom Modules

---

## 📖 What is a Module?

A module is a file containing Python code (functions, variables, classes) that can be reused in other programs.

Benefits:
- Code Reusability
- Better Organization
- Easier Maintenance

---

## 📖 Importing a Module

Python provides many built-in modules.

Example:

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

---

## 📖 Import Specific Functions

Instead of importing the entire module:

```python
from math import sqrt

print(sqrt(49))
```

Output:

```text
7.0
```

---

## 📖 Using an Alias

```python
import math as m

print(m.pi)
```

Output:

```text
3.141592653589793
```

---

## 📖 Common Built-in Modules

| Module | Purpose |
|----------|---------|
| math | Mathematical operations |
| random | Generate random values |
| datetime | Date and time operations |
| os | Operating system tasks |
| statistics | Statistical calculations |

---

## 📖 Creating a Custom Module

### mymodule.py

```python
def greet(name):
    print("Hello", name)
```

### main.py

```python
import mymodule

mymodule.greet("Sam")
```

---

## 📚 Key Points

- Modules help organize code.
- Python provides many built-in modules.
- Use `import` to load modules.
- Custom modules can be created easily.

---

## 🎯 Day 13 Completed

Modules are essential for writing scalable and reusable Python programs.
