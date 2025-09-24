from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel
import uuid


class TestSchema(BaseModel):
    url: HttpUrl
    email: EmailStr


class CourseShema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Default title is here"
    max_score: int = Field(alias="maxScore", default=123)
    min_score: int
    description: str
    estimated_time: str

    @computed_field(alias="lowcaseDescription")
    def lowcase_description(self) -> str:
        return self.description.lower()

    # === Create CourseShema object


# course_default_model = CourseShema(
#     id="123",
#     title="New version",
#     maxScore=100,
#     minScore=10,
#     description="Course Description",
#     estimatedTime="2 weeks"
# )
# print(f'{course_default_model=}')

# === From Python dict to Pydantic Model
# course_dict = {
#     "id": "string",
#     "title": "string",
#     "maxScore": 0,
#     "minScore": 0,
#     "description": "string",
#     "estimatedTime": "string",
# }
#
# course_dict_model = CourseShema(**course_dict)
# print(f'{course_dict_model=}')

# === From json-string to Pydantic model
# course_json = '''
# {
#     "id": "string",
#     "title": "string",
#     "maxScore": 0,
#     "minScore": 0,
#     "description": "string",
#     "estimatedTime": "string"
# }
# '''
# # Deserialzation
# course_json_model = CourseShema.model_validate_json(course_json)
# print(f'{course_json_model=}')
# # Serialize model to the json-string
# print(course_json_model.model_dump_json(by_alias=True))
# # Serialize model to the dict
# print(course_json_model.model_dump(by_alias=True))

# course = CourseShema(
#     min_score=3,
#     description="Here is a description",
#     estimated_time="2 weeks"
# )
# print(f'{course=}')


try:
    test_data = TestSchema(email="ert@ef.er+t.rt", url="http://localhost:8000")
    print(f"{test_data=}")
except ValidationError as e:
    print(e.errors())
