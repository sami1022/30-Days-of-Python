# Day 18 - Polymorphism 🐍

## 📌 Topics Covered
- Introduction to Polymorphism
- Method Overriding
- Polymorphism with Inheritance
- Duck Typing Concept
- Benefits of Polymorphism

---

## 📖 What is Polymorphism?

Polymorphism means **"many forms"**.

It allows different classes to use the same method name but perform different actions.

Example:

```python
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")
```

Both classes have a method named `sound()`, but the behavior is different.

---

## 📖 Method Overriding

Method overriding occurs when a child class provides its own implementation of a parent class method.

Example:

```python
class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Dog Barks")
```

---

## 📖 Polymorphism Example

```python
class Bird:

    def move(self):
        print("Flying")

class Fish:

    def move(self):
        print("Swimming")
```

Same method name, different behavior.

---

## 📖 Benefits of Polymorphism

- Improves flexibility
- Enhances code reusability
- Simplifies program structure
- Makes code easier to maintain

---

## 📚 Key Points

- Polymorphism means one interface, many implementations.
- Achieved through method overriding.
- Same method name can behave differently.
- Commonly used with inheritance.

---

## 🎯 Day 18 Completed

Polymorphism makes object-oriented programs more flexible and scalable.
