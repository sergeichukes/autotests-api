import pytest

from clients.auth.auth_client import get_auth_client, AuthClient


@pytest.fixture
def auth_client() -> AuthClient:
    return get_auth_client()
