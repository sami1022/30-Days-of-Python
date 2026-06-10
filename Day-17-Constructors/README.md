# Day 17 - Constructors 🐍

## 📌 Topics Covered
- Introduction to Constructors
- __init__ Method
- Initializing Object Attributes
- Creating Objects with Constructors
- Constructor Parameters

---

## 📖 What is a Constructor?

A constructor is a special method that is automatically called when an object is created.

In Python, the constructor method is:

```python
__init__()
```

---

## 📖 Why Use Constructors?

Constructors are used to:
- Initialize object attributes
- Assign values during object creation
- Reduce repetitive code

---

## 📖 Syntax

```python
class Student:

    def __init__(self):
        print("Constructor Called")
```

Example:

```python
student1 = Student()
```

Output:

```text
Constructor Called
```

---

## 📖 Constructor with Parameters

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Sam", 20)
```

---

## 📖 Accessing Attributes

```python
print(student1.name)
print(student1.age)
```

Output:

```text
Sam
20
```

---
# Day 17 - Constructors 🐍

## 📌 Topics Covered
- Introduction to Constructors
- __init__ Method
- Initializing Object Attributes
- Creating Objects with Constructors
- Constructor Parameters

---

## 📖 What is a Constructor?

A constructor is a special method that is automatically called when an object is created.

In Python, the constructor method is:

```python
__init__()
```

---

## 📖 Why Use Constructors?

Constructors are used to:
- Initialize object attributes
- Assign values during object creation
- Reduce repetitive code

---

## 📖 Syntax

```python
class Student:

    def __init__(self):
        print("Constructor Called")
```

Example:

```python
student1 = Student()
```

Output:

```text
Constructor Called
```

---

## 📖 Constructor with Parameters

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Sam", 20)
```

---

## 📖 Accessing Attributes

```python
print(student1.name)
print(student1.age)
```

Output:

```text
Sam
20
```

---

## 📖 Using Methods with Constructor Data

```python
class Student:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)
```

---

## 📚 Key Points

- `__init__()` is called automatically.
- Used to initialize object data.
- Parameters allow dynamic object creation.
- `self` refers to the current object.

---

## 🎯 Day 17 Completed

Constructors are essential for creating flexible and reusable classes.
## 📖 Using Methods with Constructor Data

```python
class Student:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)
```

---

## 📚 Key Points

- `__init__()` is called automatically.
- Used to initialize object data.
- Parameters allow dynamic object creation.
- `self` refers to the current object.

---

## 🎯 Day 17 Completed

Constructors are essential for creating flexible and reusable classes.
