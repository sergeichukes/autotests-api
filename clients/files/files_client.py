import sys
from typing import TypedDict
from pathlib import Path

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, UserDict


class CreateFileRequestDict(TypedDict):
    filename: str
    directory: str


class FileDict(TypedDict):
    id: str
    filename: str
    directory: str
    url: str


class CreateFileResponseDict(TypedDict):
    file: FileDict


class FileClient(APIClient):
    def get_file_api(self, file_id: str) -> Response:
        return self.get(f"/api/v1/files/{file_id}")

    def delete_file_api(self, file_id: str) -> Response:
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        file_path = Path(r"testdata/files", request["filename"])
        return self.post(
            "/api/v1/files",
            data=request,
            files={"upload_file": open(file_path, "rb")}
        )

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        response = self.create_file_api(request)
        return response.json()


def get_files_client(user: UserDict) -> FileClient:
    return FileClient(client=get_private_http_client(user))
