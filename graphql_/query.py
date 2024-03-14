from typing import List

import strawberry

from service.course import CourseService
from schema import CourseType
from middleware.jwt_bearer import IsAuthenticated


@strawberry.type
class Query:

    @strawberry.field
    def hello(self) -> str:
        return "Hello World!"

    @strawberry.field(permission_classes=[IsAuthenticated])
    async def get_all(self) -> List[CourseType]:
        return await CourseService.get_all_note()

    @strawberry.field(permission_classes=[IsAuthenticated])
    async def get_by_id(self, id: int) -> CourseType:
        return await CourseService.get_by_id(id)