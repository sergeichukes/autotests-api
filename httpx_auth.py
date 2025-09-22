import httpx

BASE_URL = "http://localhost:8000"

login_payload = {
    "email": "test@example.com",
    "password": "secretPassword"
}

response_login = httpx.post(BASE_URL + "/api/v1/authentication/login", json=login_payload)
refresh_token = response_login.json()['token']['refreshToken']
access_token = response_login.json()['token']['accessToken']

headers = {
    "Authorization": f'Bearer {access_token}'
}
response_me = httpx.get(BASE_URL + "/api/v1/users/me", headers=headers)
print(response_me.json())
