from time import time


def get_random_email() -> str:
    return f'test.{time()}@example.com'
