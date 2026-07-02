import requests

# Practice Question 1

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print("Status Code:", response.status_code)

# Practice Question 2

if response.status_code == 200:
    posts = response.json()

    print("First Post Title:")
    print(posts[0]["title"])

# Practice Question 3

response = requests.get("https://jsonplaceholder.typicode.com/todos")

if response.status_code == 200:
    todos = response.json()

    print("First Todo:")
    print(todos[0])

# Practice Question 4

response = requests.get("https://jsonplaceholder.typicode.com/comments")

print("Total Comments:", len(response.json()))

# Mini Task

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()

    print("\nUser List:")

    for user in users:
        print(user["name"], "-", user["email"])
