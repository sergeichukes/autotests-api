from typing import TypedDict

from httpx import Response, QueryParams

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, UserDict


class GetCoursesQueryDict(TypedDict):
    userId: str


class CreateCourseRequestDict(TypedDict):
    title: str
    maxScore: int | None
    minScore: int | None
    description: str
    estimatedTime: str | None
    previewFileId: str
    createdByUserId: str


class UpdateCourseRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    def get_courses_api(self, query: GetCoursesQueryDict):
        params = QueryParams(dict(query))
        return self.get("/api/v1/courses", params=params)

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        return self.post("/api/v1/courses", json=request)

    def get_course_api(self, course_id: str) -> Response:
        return self.get(f"/api/v1/courses/{course_id}")

    def delete_course_api(self, course_id: str) -> Response:
        return self.delete(f"/api/v1/courses/{course_id}")

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        return self.patch(f"/api/v1/courses/{course_id}", json=request)


def get_private_courses_client(user: UserDict) -> CoursesClient:
    return CoursesClient(client=get_private_http_client(user))
