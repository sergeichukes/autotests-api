from pydantic import BaseModel, Field
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import faker


class GetCoursesQuerySchema(BaseModel):
    userId: str


class CourseSchema(BaseModel):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: FileSchema
    estimatedTime: str
    createdByUser: UserSchema


class CreateCourseRequestSchema(BaseModel):
    title: str = Field(default_factory=faker.text)
    maxScore: int | None = None
    minScore: int | None = None
    description: str = Field(default_factory=faker.text)
    estimatedTime: str | None = None
    previewFileId: str
    createdByUserId: str


class CreateCourseResponseSchema(BaseModel):
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None
