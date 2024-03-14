from model.course import Course
from config import db
from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete


class CourseRepository:

    @staticmethod
    async def create(course_data: Course):
        async with db as session:
            async with session.begin():
                session.add(course_data)
            await db.commit_rollback()

    @staticmethod
    async def get_by_id(course_id: int):
        async with db as session:
            stmt = select(Course).where(Course.id == course_id)
            result = await session.execute(stmt)
            course = result.scalars().first()
            return course

    @staticmethod
    async def get_all():
        async with db as session:
            query = select(Course)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(course_id: int, course_data: Course):
        async with db as session:
            stmt = select(Course).where(Course.id == course_id)
            result = await session.execute(stmt)

            course = result.scalars().first()
            course.name = course_data.name
            course.description = course_data.description

            query = sql_update(Course).where(Course.id == course_id).values(
                **course.dict()).execution_options(synchronize_session="fetch")

            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def delete(note_id: int):
        async with db as session:
            query = sql_delete(Course).where(Course.id == note_id)
            await session.execute(query)
            await db.commit_rollback()