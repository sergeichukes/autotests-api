from httpx import Client
from pydantic import BaseModel

from clients.auth.auth_client import get_auth_client
from clients.auth.auth_schema import LoginRequestSchema
from clients.users.users_schema import UserSchema


class UserWithPasswordSchema(BaseModel):
    email: str
    password: str


def get_private_http_client(user: UserWithPasswordSchema) -> Client:
    auth_client = get_auth_client()
    login_request = LoginRequestSchema(
        email=str(user.email),
        password=user.password
    )
    response = auth_client.login(login_request)

    return Client(
        timeout=5,
        base_url="http://localhost:8000",
        headers={
            "Authorization": f"{response.token.token_type} {response.token.access_token}"
        }
    )
