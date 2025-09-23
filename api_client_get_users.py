from clients.users.private_users_client import get_private_users_client, UserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.tools import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="newPassword",
    lastName="Bobic",
    firstName="Bob",
    middleName="John"
)
create_user_response = public_users_client.create_user(create_user_request)
print(f"{create_user_response=}")

private_users_client = get_private_users_client(UserSchema(
    email=create_user_request["email"],
    password=create_user_request["password"]
))
get_user_data = private_users_client.get_user(create_user_response["user"]["id"])
print(f"{get_user_data=}")
