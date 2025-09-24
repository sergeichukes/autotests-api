from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

from clients.private_http_builder import get_private_http_client, UserSchema
from clients.users.users_schema import UpdateUserRequestSchema, CreateUserResponseSchema


class PrivateUsersClient(APIClient):
    def get_user_me_api(self) -> Response:
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump())

    def delete_user_api(self, user_id: str) -> Response:
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> CreateUserResponseSchema:
        response = self.get_user_api(user_id)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_private_users_client(user: UserSchema) -> PrivateUsersClient:
    return PrivateUsersClient(client=get_private_http_client(user))
