from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict


class LoginRequestDict(TypedDict):
    email: str
    password: str


class RefreshRequestDict(TypedDict):
    refreshToken: str


class AuthClient(APIClient):
    def login_api(self, request: LoginRequestDict) -> Response:
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request)
