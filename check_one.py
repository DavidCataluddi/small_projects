import requests

URL = str(input("Insert a valid URL: "))
timeout = 6

try:
    response = requests.get(URL, timeout=timeout)
    print(f"Status code = {response.status_code}")
    if response.ok:
        print("The request is OK")
    else:
        print("BAD REQUEST")
except requests.Timeout:
    print(f"Timeout after {timeout} seconds")
except requests.RequestException as e:
    print("Error during request: ", e)