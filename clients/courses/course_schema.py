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


class GetCoursesResponseSchema(BaseModel):
    courses: list[CourseSchema]


class CreateCourseRequestSchema(BaseModel):
    title: str = Field(default_factory=faker.text)
    maxScore: int | None = 10
    minScore: int | None = 1
    description: str = Field(default_factory=faker.text)
    estimatedTime: str | None = '1 week'
    previewFileId: str
    createdByUserId: str


class CreateCourseResponseSchema(BaseModel):
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    title: str | None = Field(default_factory=faker.text)
    maxScore: int | None = 200
    minScore: int | None = 100
    description: str | None = Field(default_factory=faker.text)
    estimatedTime: str | None = '2 weeks'


class UpdateCourseResponseSchema(BaseModel):
    course: CourseSchema
