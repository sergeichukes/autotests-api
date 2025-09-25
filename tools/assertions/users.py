from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal
from clients.users.users_schema import UserSchema


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.lastName, request.lastName, "lastName")
    assert_equal(response.user.firstName, request.firstName, "firstName")
    assert_equal(response.user.middleName, request.middleName, "middleName")


def asser_user(actual: UserSchema, expected: UserSchema):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")
