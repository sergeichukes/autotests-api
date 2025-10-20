import allure

from clients.courses.course_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, GetCoursesQuerySchema, \
    GetCoursesResponseSchema, CourseSchema, CreateCourseResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user


@allure.step('Check update course response')
def assert_update_course_response(request: UpdateCourseRequestSchema,
                                  response: UpdateCourseResponseSchema):
    assert_equal(response.course.title, request.title, 'title')
    assert_equal(response.course.minScore, request.minScore, 'minScore')
    assert_equal(response.course.maxScore, request.maxScore, 'maxScore')
    assert_equal(response.course.description, request.description, 'description')
    assert_equal(response.course.estimatedTime, request.estimatedTime, 'estimatedTime')


@allure.step('Check course')
def assert_course(actual: CourseSchema, expected: CourseSchema):
    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.title, expected.title, 'title')
    assert_equal(actual.maxScore, expected.maxScore, 'maxScore')
    assert_equal(actual.minScore, expected.minScore, 'minScore')
    assert_equal(actual.estimatedTime, expected.estimatedTime, 'estimatedTime')
    assert_equal(actual.description, expected.description, 'description')
    assert_file(actual.previewFile, expected.previewFile)
    assert_user(actual.createdByUser, expected.createdByUser)


@allure.step('Check get courses response')
def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_responses: list[CreateCourseResponseSchema]
):
    assert_length(get_courses_response.courses, create_course_responses, 'courses')

    for index, response in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], response.course)
