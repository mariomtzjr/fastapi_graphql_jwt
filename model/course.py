from sqlmodel import SQLModel, Field
from typing import Optional


class Course(SQLModel, table=True):
    __tablename__ = "course"

    id: Optional[int] = Field(None, primary_key=True, nullable=False)
    name: str
    description: str