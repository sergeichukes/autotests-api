from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

from clients.private_http_builder import get_private_http_client, UserSchema
from clients.users.public_users_client import CreateUserResponseDict


class UpdateUserRequestDict(TypedDict):
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class PrivateUsersClient(APIClient):
    def get_user_me_api(self) -> Response:
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> CreateUserResponseDict:
        response = self.get_user_api(user_id)
        return response.json()


def get_private_users_client(user: UserSchema) -> PrivateUsersClient:
    return PrivateUsersClient(client=get_private_http_client(user))
