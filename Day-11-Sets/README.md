# Day 11 - Sets 🐍

## 📌 Topics Covered
- Introduction to Sets
- Creating Sets
- Adding and Removing Elements
- Set Operations
- Union, Intersection, Difference
- Looping Through Sets

---

## 📖 What is a Set?

A set is a collection of unique items.

Example:

```python
fruits = {"Apple", "Banana", "Mango"}
```

Sets are:
- Unordered
- Mutable
- Do not allow duplicate values

---

## 📖 Creating a Set

```python
numbers = {1, 2, 3, 4, 5}

print(numbers)
```

Duplicate values are automatically removed.

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

Output:

```text
{1, 2, 3, 4}
```

---

## 📖 Adding Elements

```python
fruits = {"Apple", "Banana"}

fruits.add("Mango")

print(fruits)
```

---

## 📖 Removing Elements

```python
fruits.remove("Banana")
```

or

```python
fruits.discard("Banana")
```

---

## 📖 Set Operations

### Union

Combines elements from both sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
```

### Intersection

Common elements.

```python
print(a.intersection(b))
```

### Difference

Elements present in first set only.

```python
print(a.difference(b))
```

---

## 📖 Looping Through Sets

```python
fruits = {"Apple", "Banana", "Mango"}

for fruit in fruits:
    print(fruit)
```

---

## 📚 Key Points

- Sets store unique values.
- Duplicate values are removed automatically.
- Sets support mathematical operations.
- Sets are unordered.

---

## 🎯 Day 11 Completed

Sets are useful when working with unique data and performing set operations.
