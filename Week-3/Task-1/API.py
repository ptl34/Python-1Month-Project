import requests

# Fetch user data from API
response = requests.get("https://randomuser.me/api")

# Convert to Python dictionary
data = response.json()

# Extract needed info
user = data['results'][0]
name = f"{user['name']['first']} {user['name']['last']}"
gender = user['gender']
email = user['email']

# Display it
print("Random User Info:")
print(f"Name   : {name}")
print(f"Gender : {gender}")
print(f"Email  : {email}")
