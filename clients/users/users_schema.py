from pydantic import BaseModel, EmailStr, Field
from tools.fakers import faker


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseSchema(BaseModel):
    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    email: str = Field(default_factory=faker.email)
    password: str = Field(default_factory=faker.text)
    lastName: str = Field(default_factory=faker.text)
    firstName: str = Field(default_factory=faker.text)
    middleName: str = Field(default_factory=faker.text)


class UpdateUserRequestSchema(BaseModel):
    email: EmailStr | None
    lastName: str | None
    firstName: str | None
    middleName: str | None
