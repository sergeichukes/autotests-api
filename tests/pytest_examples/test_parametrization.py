import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [-1, 1, 2, 4])
def test_numbers(number: int):
    assert number > 0


# @pytest.mark.parametrize("number", "expected", [(1, 1), (2, 4)])
# def test_several_numbers(number: int, expected: int):
#     assert number ** 2 == expected


@pytest.mark.parametrize('os',
                         ['macos', 'windows', 'linux'],
                         ids=["System macos", "System Windows XP", "System linux"])
@pytest.mark.parametrize('host', ['prod', 'stable', 'dev'])
def test_mult_of_numbers(os: str, host: str):
    assert len(os + host) > 0


@pytest.fixture(params=['prod', 'stable', 'dev'])
def host(request: SubRequest) -> str:
    return request.param


def test_host(host: str):
    print(f"Running with: {host}")


class TestOperations:
    def test_user_with_operations(self):
        print('User with operation')

    def test_user_without_operations(self):
        print('User withOUT operation')
