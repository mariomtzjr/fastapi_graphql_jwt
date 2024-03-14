from model.course import Course
from repository.course import CourseRepository
from schema import CourseInput, CourseType


class CourseService:

    @staticmethod
    async def add_note(course_data: CourseInput):
        course = Course()
        course.name = course_data.name
        course.description = course_data.description
        await CourseRepository.create(course)

        return CourseType(id=course.id, name=course.name, description=course.description)

    @staticmethod
    async def get_all_note():
        list_courses = await CourseRepository.get_all()
        return [CourseType(id=course.id, name=course.name, description=course.description) for course in list_courses]

    @staticmethod
    async def get_by_id(course_id: int):
        course = await CourseRepository.get_by_id(course_id)
        return CourseType(id=course.id, name=course.name, description=course.description)

    @staticmethod
    async def delete(course_id: int):
        await CourseRepository.delete(course_id)
        return f'Successfully deleted data by id {course_id}'

    @staticmethod
    async def update(course_id:int, course_data: CourseInput):
        course = Course()
        course.name = course_data.name
        course.description = course_data.description
        await course_data.update(course_id, course)

        return f'Successfully updated data by id {course_id}'