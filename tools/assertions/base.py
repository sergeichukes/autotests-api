from typing import Any, Sized


def assert_status_code(actual: int, expected: int):
    assert actual == expected, (
        'Incorrect response status code. '
        f'Expected: {expected}, but actual: {actual}'
    )


def assert_equal(actual: Any, expected: Any, name: str) -> None:
    assert actual == expected, (
        f'Incorrect value "{name}": '
        f'Expected: {expected}'
        f'Actual: {actual}'
    )


def assert_is_true(actual: Any, name: str) -> None:
    assert actual, (
        f'Incorrect value "{name}": '
        f'Expected true value but got: {actual}'
    )


def assert_length(actual: Sized, expected: Sized, name):
    assert len(actual) == len(expected), (
        f'Incorrect object length "{name}": '
        f'Expected: {len(expected)}'
        f'Actual: {len(actual)}'
    )
