from pydantic import BaseModel, Field, ConfigDict, EmailStr
from pydantic.alias_generators import to_camel


class TokenSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    token_type: str
    access_token: str
    refresh_token: str


class LoginRequestSchema(BaseModel):
    email: str
    password: str


class RefreshRequestSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    refresh_token: str


class LoginResponseSchema(BaseModel):
    token: TokenSchema
