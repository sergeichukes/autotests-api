from pydantic import BaseModel, HttpUrl, Field
from tools.fakers import faker


class CreateFileRequestSchema(BaseModel):
    filename: str = Field(default_factory=lambda: f'{faker.text()}.png')
    directory: str = 'files'


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CreateFileResponseSchema(BaseModel):
    file: FileSchema
