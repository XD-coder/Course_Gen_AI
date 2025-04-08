import requests

# Define the data payload as a dictionary
payload = {
    'course_name': 'AI_with_pyhton',
    'course_duration': '3 months',
    'course_level': 'beginner'
}

# Send a POST request with the data in the JSON body
response = requests.post('http://127.0.0.1:8000/generate', json=payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text) # Print error details from the server

    