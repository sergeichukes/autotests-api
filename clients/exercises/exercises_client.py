from typing import TypedDict

from httpx import Response, QueryParams

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, UserDict

BASE_EXERCISES_URI = "/api/v1/exercises"


class GetExercisesQueryDict(TypedDict):
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int | None
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    title: str | None
    courseId: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        params = QueryParams(dict(query))
        return self.get(BASE_EXERCISES_URI, params=params)

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        return self.post(BASE_EXERCISES_URI, json=request)

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(BASE_EXERCISES_URI + f"/{exercise_id}")

    def delete_exercise_api(self, exercise_id: str) -> Response:
        return self.delete(BASE_EXERCISES_URI + f"/{exercise_id}")

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        return self.patch(BASE_EXERCISES_URI + f"/{exercise_id}", json=request)


def get_exercises_client(user: UserDict) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))
