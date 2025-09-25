import pytest


class TestUserFlow:
    def test_user_can_login(self, settings, user, users_client):
        ...

    def test_user_can_create_course(self, user, settings, users_client):
        ...


class TestAccountFlow:
    def test_user_account(self, user, settings, users_client):
        ...


@pytest.fixture(scope="session")
def user_data():
    print("Создаем пользователя ДО теста")
    yield {
        "email": "dfd",
        "age": 30
    }
    print('Удаляем пользоавтеля ПОСЛЕ теста')


def test_user_email(user_data: dict):
    print(user_data)
    assert user_data['email'] == "dfd"


def test_user_age(user_data: dict):
    print(user_data)
    assert user_data['age'] == 30
