from httpx import Client

from clients.auth.auth_client import get_auth_client, LoginRequestDict
from typing import TypedDict


class UserDict(TypedDict):
    email: str
    password: str


def get_private_http_client(user: UserDict) -> Client:
    auth_client = get_auth_client()
    response = auth_client.login(user)

    return Client(
        timeout=5,
        base_url="http://localhost:8000",
        headers={
            "Authorization": f"{response['token']['tokenType']} {response["token"]["accessToken"]}"
        }
    )
