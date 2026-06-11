# Day 17 - Inheritance 🐍

## 📌 Topics Covered
- Introduction to Inheritance
- Parent Class
- Child Class
- Types of Inheritance
- Method Inheritance

---

## 📖 What is Inheritance?

Inheritance is an OOP concept where one class acquires the properties and methods of another class.

Benefits:
- Code Reusability
- Reduced Redundancy
- Easier Maintenance

---

## 📖 Parent Class

A parent class (base class) contains common properties and methods.

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")
```

---

## 📖 Child Class

A child class inherits from the parent class.

```python
class Dog(Animal):
    pass
```

Now `Dog` can use methods of `Animal`.

```python
dog = Dog()
dog.sound()
```

Output:

```text
Animal makes a sound
```

---

## 📖 Adding New Methods

```python
class Dog(Animal):

    def bark(self):
        print("Dog barks")
```

---

## 📖 Types of Inheritance

- Single Inheritance
- Multiple Inheritance
- Multilevel Inheritance
- Hierarchical Inheritance

For now, focus on Single Inheritance.

---

## 📚 Key Points

- Child classes inherit parent class features.
- Promotes code reuse.
- Child classes can add their own methods.
- Parent methods can be directly accessed.

---

## 🎯 Day 17 Completed

Inheritance is one of the core pillars of Object-Oriented Programming.
