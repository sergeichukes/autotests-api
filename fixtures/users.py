import pytest
from pydantic import BaseModel

from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> str:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def auth_user(self) -> UserSchema:
        return self.response.user


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()


@pytest.fixture()
def private_users_client(function_user) -> PrivateUsersClient:
    return get_private_users_client(function_user.auth_user)


@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)
