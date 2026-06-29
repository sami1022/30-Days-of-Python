# Day 25 - Regular Expressions (Regex) 🐍

## 📌 Topics Covered
- Introduction to Regular Expressions
- The `re` Module
- Pattern Matching
- Common Regex Functions
- Regex Metacharacters
- Practical Examples

---

## 📖 What is a Regular Expression?

A **Regular Expression (Regex)** is a sequence of characters used to search, match, and manipulate text.

Python provides the built-in **`re`** module for working with regular expressions.

```python
import re
```

---

## 📖 Common Regex Functions

| Function | Description |
|----------|-------------|
| `re.search()` | Searches for the first match |
| `re.match()` | Matches from the beginning of the string |
| `re.findall()` | Returns all matches |
| `re.sub()` | Replaces matched text |
| `re.split()` | Splits a string using a pattern |

---

## 📖 Example: Search

```python
import re

text = "Python is awesome"

result = re.search("Python", text)

if result:
    print("Match Found")
```

Output:

```text
Match Found
```

---

## 📖 Example: Find All Numbers

```python
import re

text = "Age: 20, Marks: 95"

numbers = re.findall(r"\d+", text)

print(numbers)
```

Output:

```text
['20', '95']
```

---

## 📖 Example: Replace Text

```python
import re

text = "I like Java"

new_text = re.sub("Java", "Python", text)

print(new_text)
```

Output:

```text
I like Python
```

---

## 📖 Common Regex Patterns

| Pattern | Meaning |
|---------|---------|
| `\d` | Digit (0–9) |
| `\D` | Non-digit |
| `\w` | Letter, digit or underscore |
| `\W` | Special character |
| `\s` | Whitespace |
| `.` | Any character |
| `^` | Start of string |
| `$` | End of string |

---

## 📚 Key Points

- Regex helps search and manipulate text.
- Python uses the `re` module.
- `findall()` returns all matching patterns.
- `sub()` replaces matching text.
- Regex is widely used in data validation and text processing.

---

## 🎯 Day 25 Completed

Regular Expressions are essential for validating emails, phone numbers, passwords, extracting data, and cleaning text.
