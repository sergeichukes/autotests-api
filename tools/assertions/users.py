from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.lastName, request.lastName, "lastName")
    assert_equal(response.user.firstName, request.firstName, "firstName")
    assert_equal(response.user.middleName, request.middleName, "middleName")
