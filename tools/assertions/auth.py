from clients.auth.auth_schema import LoginResponseSchema
from tools.assertions.base import assert_equal, assert_is_true


def assert_login_response(response: LoginResponseSchema) -> None:
    assert_equal(response.token.token_type, 'bearer', 'token_type')
    assert_is_true(response.token.access_token, 'access_token')
    assert_is_true(response.token.refresh_token, 'refresh_token')
