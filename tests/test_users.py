import pytest

from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus

from tools.assertions.base import assert_status_code

from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response
from tools.fakers import faker


@pytest.mark.users
@pytest.mark.regression
@pytest.mark.parametrize('domain', ['mail.ru', 'gmail.com', 'example.com'])
def test_create_user(public_users_client: PublicUsersClient, domain: str):
    request = CreateUserRequestSchema(
        email=faker.email(domain)
    )
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data)

    validate_json_schema(instance=response_data.model_dump(), schema=CreateUserResponseSchema.model_json_schema())
