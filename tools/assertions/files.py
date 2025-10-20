import allure

from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, \
    GetFileResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response


@allure.step('Check create file response')
def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    expected_url = f'http://localhost:8000/static/{request.directory}/{request.filename}'

    assert_equal(response.file.filename, request.filename, 'filename')
    assert_equal(response.file.directory, request.directory, 'directory')
    assert_equal(str(response.file.url), expected_url, 'url')


@allure.step('Check file')
def assert_file(actual: FileSchema, expected: FileSchema):
    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.filename, expected.filename, 'filename')
    assert_equal(actual.directory, expected.directory, 'directory')
    assert_equal(actual.url, expected.url, 'url')


@allure.step('Check get file response')
def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    assert_file(get_file_response.file, create_file_response.file)


@allure.step('Check create file with empty filename response')
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type='string_too_short',
                input='',
                context={'min_length': 1},
                message='String should have at least 1 character',
                location=['body', 'filename']
            )
        ]
    )

    assert_validation_error_response(actual, expected)


@allure.step('Check create file with empty directory response')
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type='string_too_short',
                input='',
                context={'min_length': 1},
                message='String should have at least 1 character',
                location=['body', 'directory']
            )
        ]
    )

    assert_validation_error_response(actual, expected)


@allure.step('Check file not found response')
def assert_file_not_found_response(
        actual: InternalErrorResponseSchema,
):
    expected = InternalErrorResponseSchema(detail="File not found")
    assert_internal_error_response(actual, expected)
