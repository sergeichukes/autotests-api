from pydantic import BaseModel, HttpUrl


class CreateFileRequestSchema(BaseModel):
    filename: str
    directory: str


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CreateFileResponseSchema(BaseModel):
    file: FileSchema
