# Day 20 - Abstraction 🐍

## 📌 Topics Covered
- Introduction to Abstraction
- Abstract Classes
- Abstract Methods
- abc Module
- Benefits of Abstraction

---

## 📖 What is Abstraction?

Abstraction means hiding implementation details and showing only the essential features to the user.

Real-life example:
- When you drive a car, you use the steering wheel, brake, and accelerator.
- You don't need to know the internal engine implementation.

---

## 📖 Why Use Abstraction?

Abstraction helps:
- Reduce complexity
- Improve security
- Focus on important features
- Create cleaner code

---

## 📖 Abstract Class

Python provides the `abc` module for abstraction.

```python
from abc import ABC, abstractmethod
```

An abstract class cannot be instantiated directly.

---

## 📖 Abstract Method

An abstract method must be implemented by child classes.

Example:

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

## 📖 Implementing Abstract Methods

```python
class Dog(Animal):

    def sound(self):
        print("Dog Barks")
```

Usage:

```python
dog = Dog()
dog.sound()
```

Output:

```text
Dog Barks
```

---

## 📚 Key Points

- Abstraction hides implementation details.
- Use the `abc` module.
- Abstract classes contain abstract methods.
- Child classes must implement abstract methods.

---

## 🎯 Day 20 Completed

Abstraction is one of the four pillars of Object-Oriented Programming and helps build scalable applications.
