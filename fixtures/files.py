import pytest
from pydantic import BaseModel

from clients.files.files_client import get_files_client, FileClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.users import UserFixture


class FileFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema


@pytest.fixture
def files_client(function_user: UserFixture) -> FileClient:
    return get_files_client(function_user.auth_user)


@pytest.fixture
def function_file(files_client: FileClient) -> FileFixture:
    request = CreateFileRequestSchema(filename="image.png")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)
