import allure

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal
from clients.users.users_schema import UserSchema


@allure.step('Check create user response')
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.lastName, request.lastName, "lastName")
    assert_equal(response.user.firstName, request.firstName, "firstName")
    assert_equal(response.user.middleName, request.middleName, "middleName")


@allure.step('Check user')
def assert_user(actual: UserSchema, expected: UserSchema):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.lastName, expected.lastName, "lastName")
    assert_equal(actual.firstName, expected.firstName, "firstName")
    assert_equal(actual.middleName, expected.middleName, "middleName")
