from httpx import Client
from pydantic import BaseModel, ConfigDict
from functools import lru_cache

from clients.auth.auth_client import get_auth_client
from clients.auth.auth_schema import LoginRequestSchema


class UserSchema(BaseModel):
    model_config = ConfigDict(frozen=True)

    email: str
    password: str


@lru_cache(maxsize=None)
def get_private_http_client(user: UserSchema) -> Client:
    auth_client = get_auth_client()
    login_request = LoginRequestSchema(
        email=user.email,
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
