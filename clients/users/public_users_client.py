from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient

from clients.public_http_builder import get_public_http_client


class CreateUserRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        return self.post("/api/v1/users", json=request)


def get_public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=get_public_http_client())
