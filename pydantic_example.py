from pydantic import BaseModel, Field


class AddressSchema(BaseModel):
    city: str
    zip_code: int


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias="isActive")


user_data = {
    'id': 1,
    'name': 'Alice',
    'email': 'es@example.com',
    'isActive': True
}

user = User(**user_data)
print(user.model_dump(by_alias=True))
