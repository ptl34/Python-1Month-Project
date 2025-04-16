import requests
import json

# Fetch random user data from RandomUserAPI
url = "https://randomuser.me/api/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract user data from the response
    data = response.json()
    user = data['results'][0]  # Get the first random user

    # Save the fetched data to a JSON file
    with open("user_data.json", "w") as json_file:
        json.dump(data, json_file)

    # Load and display the saved data
    with open("user_data.json", "r") as json_file:
        saved_data = json.load(json_file)
        saved_user = saved_data['results'][0]

        # Extracting name, gender, and email from saved data
        saved_name = saved_user['name']['first'] + " " + saved_user['name']['last']
        saved_gender = saved_user['gender']
        saved_email = saved_user['email']

        # Display the saved data
        print("\nSaved User Data:")
        print(f"Name: {saved_name}")
        print(f"Gender: {saved_gender}")
        print(f"Email: {saved_email}")
else:
    print("Failed to retrieve data")
    
