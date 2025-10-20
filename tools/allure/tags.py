from enum import Enum


class AllureTag(str, Enum):
    USERS = "USERS"
    FILES = "FILES"
    COURSES = "COURSES"
    EXERCISES = "EXERCISES"
    AUTHENTICATION = "AUTHENTICATION"

    REGRESSION = "REGRESSION"
