import httpx

BASE_URL = "http://localhost:8000"

login_payload = {
    "email": "test@example.com",
    "password": "secretPassword"
}

response_login = httpx.post(BASE_URL + "/api/v1/authentication/login", json=login_payload)
refresh_token = response_login.json()['token']['refreshToken']

refresh_payload = {
    'refreshToken': refresh_token
}
response_refresh = httpx.post(BASE_URL + "/api/v1/authentication/refresh", json=refresh_payload)
print(response_refresh.status_code, ' ', response_refresh.json())
