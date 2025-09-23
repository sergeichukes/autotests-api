from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class LoginRequestDict(TypedDict):
    email: str
    password: str


class RefreshRequestDict(TypedDict):
    refreshToken: str


class TokenDict(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str


class LoginResponseDict(TypedDict):
    token: TokenDict


class AuthClient(APIClient):
    def login_api(self, request: LoginRequestDict) -> Response:
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request)
        return response.json()


def get_auth_client() -> AuthClient:
    return AuthClient(client=get_public_http_client())
