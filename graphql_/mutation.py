import strawberry

from middleware.jwt_bearer import IsAuthenticated
from service.course import CourseService
from service.authentication import AuthenticationService
from schema import CourseType, CourseInput, RegisterInput, LoginInput, LoginType


@strawberry.type
class Mutation:

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def create_course(self, course_data: CourseInput) -> CourseType:
        return await CourseService.add_course(course_data)

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def delete_course(self, course_id: int) -> str:
        return await CourseService.delete(course_id)

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def update_course(self, course_id: int, course_data: CourseInput) -> str:
        return await CourseService.update(course_id, course_data)

    @strawberry.mutation
    async def login(self, login_data: LoginInput) -> LoginType:
        return await AuthenticationService.login(login_data)

    @strawberry.mutation
    async def register(self, register_data: RegisterInput) -> str:
        return await AuthenticationService.register(register_data)