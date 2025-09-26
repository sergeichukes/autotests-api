from typing import TypedDict

from httpx import Response, QueryParams

from clients.api_client import APIClient
from clients.files.files_schema import FileSchema
from clients.private_http_builder import get_private_http_client, UserSchema
from clients.courses.course_schema import GetCoursesQuerySchema, CreateCourseRequestSchema, UpdateCourseRequestSchema, \
    CreateCourseResponseSchema


class CoursesClient(APIClient):
    def get_courses_api(self, query: GetCoursesQuerySchema):
        return self.get("/api/v1/courses", params=QueryParams(query.model_dump()))

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        return self.post("/api/v1/courses", json=request.model_dump())

    def get_course_api(self, course_id: str) -> Response:
        return self.get(f"/api/v1/courses/{course_id}")

    def delete_course_api(self, course_id: str) -> Response:
        return self.delete(f"/api/v1/courses/{course_id}")

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        return self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump())

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


def get_courses_client(user: UserSchema) -> CoursesClient:
    return CoursesClient(client=get_private_http_client(user))
