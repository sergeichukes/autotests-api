from clients.private_http_builder import UserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.tools import get_random_email
from tools.assertions.schema import validate_json_schema
import jsonschema

public_users_client = get_public_users_client()
# Create a user
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="newPassword",
    lastName="Bobic",
    firstName="Bob",
    middleName="John"
)
create_user_response = public_users_client.create_user_api(create_user_request)
print(f"{create_user_response=}")
user = UserSchema(email=create_user_request.email, password=create_user_request.password)

schema = CreateUserResponseSchema.model_json_schema()
json_response = create_user_response.json()

validate_json_schema(instance=json_response, schema=schema)
