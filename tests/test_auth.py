import pytest

from clients.auth.auth_client import AuthClient
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import PublicUsersClient
from http import HTTPStatus

from fixtures.users import UserFixture
from tools.assertions.auth import assert_login_response
from tools.assertions.base import assert_status_code

from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.auth
def test_login(public_users_client: PublicUsersClient, auth_client: AuthClient, function_user: UserFixture):
    request = LoginRequestSchema(
        email=function_user.email,
        password=function_user.password
    )
    response = auth_client.login_api(request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)
    validate_json_schema(instance=response_data.model_dump(by_alias=True),
                         schema=LoginResponseSchema.model_json_schema())
