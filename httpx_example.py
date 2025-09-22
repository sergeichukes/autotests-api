import httpx

# === GET example
# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
# print("GET todos: ")
# print(response.status_code)
# print(response.json())

# === POST example. Using json to send the POST request
# body_data = {
#     "title": "Lena Новая задача",
#     "completed": False,
#     "userId": 1
# }
#
# response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=body_data)
# print("POST with json body: ")
# print(response.status_code)
# print(response.json())

# === POST multipart/form-urlencoded
# form_data = {
#     "username": "LenaUser",
#     "password": "LenaPassword"
# }
#
# response = httpx.post("https://httpbin.org/post", data=form_data)
# print("POST with data body multipart/form-urlencoded: ")
# print(response.status_code)
# print(response.json())

# === Add custom headers to the request
# custom_headers = {
#     "Authorization": "Bearer lena_token"
# }
# response = httpx.get("https://httpbin.org/get", headers=custom_headers)
# print("GET with custom headers")
# print(response.request.headers)
# print(response.json())

# === GET with query parameters
# query_params = {
#     "userId": 1
# }
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=query_params)
# print("GET with query parameters")
# print(response.url)
# print(response.json())


# === Work with files. Multipart-formdata
# files = {
#     "file": ("example.txt", open("example.txt", "rb"))
# }
# response = httpx.post("https://httpbin.org/post", files=files)
# print("POST, Work with files")
# print(response.json())


# === Session in http
# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
# print("Session in http")
# print(response1.json())
# print(response2.json())


# === Common headers for many requests
# client = httpx.Client(headers={'My-Header': 'this is my header'})
# response = client.get('https://httpbin.org/get')
# print("Common headers for many requests")
# print(response.json())

# ==== Errors in HTTPX
# try:
#     response = httpx.get("https://httpbin.org/invalid-url")
#     response.raise_for_status()
# except httpx.HTTPStatusError as e:
#     print(f'Ошибка запроса: {e}')

# === Timeouts in HTTPX
# try:
#     response = httpx.get("https://httpbin.org/delay/5", timeout=1)
#     print(response.status_code)
# except httpx.ReadTimeout:
#     print('Timeout was reached')
