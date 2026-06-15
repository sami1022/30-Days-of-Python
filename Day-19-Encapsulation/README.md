# Day 19 - Encapsulation 🐍

## 📌 Topics Covered
- Introduction to Encapsulation
- Public Variables
- Protected Variables
- Private Variables
- Getter and Setter Methods

---

## 📖 What is Encapsulation?

Encapsulation is the process of wrapping data (variables) and methods (functions) into a single unit (class).

It helps:
- Protect data from accidental modification
- Improve security
- Control access to class attributes

---

## 📖 Types of Access Modifiers

### Public Members

Can be accessed from anywhere.

```python
class Student:

    name = "Sam"
```

---

### Protected Members

Defined using a single underscore `_`.

```python
class Student:

    _course = "Python"
```

Protected members should only be accessed within the class and its subclasses.

---

### Private Members

Defined using double underscores `__`.

```python
class Student:

    __age = 20
```

Private members cannot be accessed directly outside the class.

---

## 📖 Getter and Setter Methods

Used to access and modify private data safely.

Example:

```python
class Student:

    def __init__(self):
        self.__age = 20

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
```

---

## 📖 Why Encapsulation?

- Data Hiding
- Better Security
- Better Control
- Cleaner Code

---

## 📚 Key Points

- Encapsulation combines data and methods.
- Private variables use `__`.
- Protected variables use `_`.
- Getter and Setter methods provide controlled access.

---

## 🎯 Day 19 Completed

Encapsulation is one of the four pillars of Object-Oriented Programming and helps create secure applications.
