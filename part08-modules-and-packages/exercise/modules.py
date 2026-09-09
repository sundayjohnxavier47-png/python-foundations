import random
print(random.randint(1, 50))

import datetime
print(datetime.datetime.now())

import requests
response = requests.get("https://api.github.com")
print(response.status_code)

response2 = requests.get("https://api.github.com/users/octocat")
data = response2.json()
print(data)
print(data["name"])