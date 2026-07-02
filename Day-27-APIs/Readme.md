# Day 27 - APIs 🐍

## 📌 Topics Covered
- Introduction to APIs
- HTTP Methods
- Installing the `requests` Library
- Sending GET Requests
- Parsing JSON Responses
- Handling API Errors

---

## 📖 What is an API?

An **API (Application Programming Interface)** allows different software applications to communicate with each other.

Examples:
- Weather Apps
- Google Maps
- Payment Gateways
- Social Media Platforms

---

## 📖 HTTP Methods

| Method | Purpose |
|---------|---------|
| GET | Retrieve data |
| POST | Create new data |
| PUT | Update existing data |
| DELETE | Remove data |

---

## 📖 Installing Requests

The most popular library for working with APIs is `requests`.

Install it using:

```bash
pip install requests
```

Import it:

```python
import requests
```

---

## 📖 Sending a GET Request

```python
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)
```

---

## 📖 Reading JSON Data

```python
data = response.json()

print(data)
```

Accessing values:

```python
print(data[0]["name"])
```

---

## 📖 Handling Errors

```python
if response.status_code == 200:
    print("Request Successful")
else:
    print("Something went wrong")
```

---

## 📚 Key Points

- APIs allow applications to communicate.
- `requests` is the most commonly used Python library for APIs.
- `response.json()` converts API responses into Python objects.
- Always check the HTTP status code before processing data.

---

## 🎯 Day 27 Completed

APIs are essential for web development, automation, data science, and machine learning projects.
