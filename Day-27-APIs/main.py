import requests

# GET Request

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    users = response.json()

    print("\nFirst User:")
    print("Name:", users[0]["name"])
    print("Email:", users[0]["email"])
    print("City:", users[0]["address"]["city"])
else:
    print("Failed to fetch data.")
