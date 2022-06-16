import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'

response = requests.get(url)
print(response)
print(dir(response))

response.raise_for_status()
print(response.status_code)

print(response.json()) #{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
print(response.ok) #True
print(response.text) #too long
print(response.url) #https://jsonplaceholder.typicode.com/todos/1
print(response.headers) #too long
print(response.content) #b'{\n  "userId": 1,\n  "id": 1,\n  "title": "delectus aut autem",\n  "completed": false\n}'

