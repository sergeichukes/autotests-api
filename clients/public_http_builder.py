from httpx import Client


def get_public_http_client() -> Client:
    return Client(timeout=5, base_url="http://locahost:8000")
