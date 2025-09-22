import httpx

login_payload = {
    "email": "test@example.com",
    "password": "secretPassword"
}

response_login = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
refresh_token = response_login.json()['token']['refreshToken']
access_token = response_login.json()['token']['accessToken']

client = httpx.Client(
    base_url='http://localhost:8000',
    timeout=30,
    headers={
        'Authorization': f'Bearer {access_token}'
    }
)

get_user_me_response = client.get('/api/v1/users/me')

print(get_user_me_response.json())
