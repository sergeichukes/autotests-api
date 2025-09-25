from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import get_files_client
from clients.users.private_users_client import get_private_users_client, UserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.files.files_schema import CreateFileRequestSchema
from tools.fakers import faker

public_users_client = get_public_users_client()

# Create a user
create_user_request = CreateUserRequestSchema(
    email=faker(),
    password="newPassword",
    lastName="Bobic",
    firstName="Bob",
    middleName="John"
)
create_user_response = public_users_client.create_user(create_user_request)
print(f"{create_user_response=}")
user = UserSchema(email=create_user_request.email, password=create_user_request.password)

# Create a file
files_client = get_files_client(user)

files_response = files_client.create_file(CreateFileRequestSchema(
    filename="image.png",
    directory="courses"))
print(f'{files_response=}')

# Create a course
courses_client = get_courses_client(user)
course_response = courses_client.create_course(CreateCourseRequestDict(
    title="Новый курс",
    minScore=10,
    maxScore=100,
    description="Новый курс про грумминг собачек",
    estimatedTime="Пять часов",
    previewFileId=files_response.file.id,
    createdByUserId=create_user_response.user.id
))
print()
print(f'{course_response=}')
