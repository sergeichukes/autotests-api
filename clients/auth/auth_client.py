from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema, RefreshRequestSchema


class AuthClient(APIClient):
    def login_api(self, request: LoginRequestSchema) -> Response:
        return self.post("/api/v1/authentication/login", json=request.model_dump())

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request.model_dump())

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)


def get_auth_client() -> AuthClient:
    return AuthClient(client=get_public_http_client())
