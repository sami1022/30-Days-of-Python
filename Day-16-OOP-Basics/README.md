# Day 16 - OOP Basics 🐍

## 📌 Topics Covered
- Introduction to OOP
- Classes and Objects
- Attributes
- Methods
- Creating Objects

---

## 📖 What is OOP?

OOP (Object-Oriented Programming) is a programming paradigm based on objects and classes.

Benefits:
- Code Reusability
- Better Organization
- Easier Maintenance
- Real-World Modeling

---

## 📖 What is a Class?

A class is a blueprint for creating objects.

Example:

```python
class Student:
    pass
```

---

## 📖 What is an Object?

An object is an instance of a class.

Example:

```python
student1 = Student()
```

---

## 📖 Attributes

Attributes store data related to an object.

Example:

```python
class Student:
    name = "Sam"
```

---

## 📖 Methods

Methods are functions defined inside a class.

Example:

```python
class Student:

    def greet(self):
        print("Hello Student")
```

The `self` parameter refers to the current object.

---

## 📖 Creating an Object

```python
class Student:

    def greet(self):
        print("Welcome")

student1 = Student()

student1.greet()
```

Output:

```text
Welcome
```

---

## 📚 Key Points

- Class = Blueprint
- Object = Instance of a class
- Attributes store data.
- Methods define behavior.
- `self` refers to the current object.

---

## 🎯 Day 16 Completed

OOP is one of the most important concepts in Python and is widely used in real-world applications.
