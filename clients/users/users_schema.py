from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseSchema(BaseModel):
    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class UpdateUserRequestSchema(BaseModel):
    email: EmailStr | None
    lastName: str | None
    firstName: str | None
    middleName: str | None
