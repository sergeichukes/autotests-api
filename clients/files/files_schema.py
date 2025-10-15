from pydantic import BaseModel, HttpUrl, Field
from tools.fakers import faker


class CreateFileRequestSchema(BaseModel):
    filename: str = 'image.png'
    directory: str = 'tests'


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CreateFileResponseSchema(BaseModel):
    file: FileSchema


class GetFileResponseSchema(BaseModel):
    file: FileSchema
