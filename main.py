import requests

# Set the host and port
host = "0.0.0.0"
port = 8080

# URL to send the request to
# Replace "greeting" with the appropriate route
url = f"http://{host}:{port}/greeting"

url1 = f"http://{host}:{port}/employee"
header1 = {
    "Content-Type": "application/json"
}
data1 = {
    "name": "Name",
    "city": "City"
}
url2 = f"http://{host}:{port}/employee/<id>"  # Replace "id" with a number

url3 = f"http://{host}:{port}/employees/all"

url4 = f"http://{host}:{port}/employee/<id>"  # Replace "id" with a number
header4 = {
    "Content-Type": "application/json"
}
data4 = {
    "name": "Name",
    "city": "City"
}

url5 = f"http://{host}:{port}/employee/<id>"  # Replace "id" with a number

try:
    # Send the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        print("Request successful!")
        print("Response content:")
        print(response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

try:
    # Send the POST request with JSON data
    response = requests.post(url1, json=data1, headers=header1)

    # Check if the request was successful
    if response.status_code == 201:
        print("Request successful!")
        print("Response content:")
        print(response.json())
    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

try:
    # Send the GET request
    response = requests.get(url2)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Request successful!")
        print("Response content:")
        print(response.json())

    # Check if the employee was not found (status code 404)
    elif response.status_code == 404:
        error_message = response.json().get("message", "Employee not found")
        print(f"Employee not found: {error_message}")

    # Handle other status codes if needed

    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

try:
    response = requests.get(url3)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Request successful!")
        print("Response content:")
        print(response.json())
    else:
        print(f"Request failed with status code: {response.status_code}")
except:
    print(f"Request failed with status code: Fail")

try:
    # Send the PUT request with JSON data
    response = requests.put(url4, json=data4, headers=header4)

    # Check if the request was successful
    if response.status_code == 201:
        print("Request successful!")
        print("Response content:")
        print(response.json())
    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

try:
    response = requests.delete(url5)

    if response.status_code == 200:
        print("Request successful!")
        print("Response content:")
        print(response.json())
    elif response.status_code == 404:
        # print("Not Found")
        error_message = response.json().get("message", "Employee not found")
        print(f"Employee not found: {error_message}")
    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
