# Day 15 - Exception Handling 🐍

## 📌 Topics Covered
- Introduction to Exceptions
- try and except
- else Block
- finally Block
- Handling Multiple Exceptions
- Raising Exceptions

---

## 📖 What is Exception Handling?

An exception is an error that occurs during program execution.

Without exception handling, the program may terminate unexpectedly.

Exception handling allows us to:
- Prevent program crashes
- Handle errors gracefully
- Improve user experience

---

## 📖 try and except

Syntax:

```python
try:
    # risky code
except:
    # error handling code
```

Example:

```python
try:
    num = int(input("Enter a number: "))
    print(num)
except:
    print("Invalid Input!")
```

---

## 📖 Handling Specific Exceptions

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## 📖 else Block

The `else` block executes when no exception occurs.

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid Input")
else:
    print("You entered:", num)
```

---

## 📖 finally Block

The `finally` block always executes.

```python
try:
    print("Running")
except:
    print("Error")
finally:
    print("Program Ended")
```

---

## 📖 Raising Exceptions

You can create your own exceptions using `raise`.

```python
age = -1

if age < 0:
    raise ValueError("Age cannot be negative")
```

---

## 📚 Key Points

- Exceptions are runtime errors.
- `try` contains risky code.
- `except` handles errors.
- `else` runs if no error occurs.
- `finally` always executes.

---

## 🎯 Day 15 Completed

Exception handling makes programs more reliable and professional.
