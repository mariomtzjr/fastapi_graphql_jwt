import os

from sqlalchemy.ext.asyncio  import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from sqlmodel import SQLModel
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = os.getenv('DB_CONFIG', '')

class DatabaseSession:
    def __init__(self, url: str=DB_CONFIG):
        self.engine = create_async_engine(url, echo=True)
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
    
    # Generation of models into database
    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
    
    async def drop_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)
    
    # Close database connection
    async def close(self):
        await self.engine.dispose()
    
    async def __aenter__(self) -> AsyncSession:
        """This function prepares the context for
        the asynchronous operation

        Returns:
            AsyncSession: Session for context
        """
        self.session = self.SessionLocal()
        return self.session

    # Method that is used to clean up resources, etc.
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
    
    async def get_db(self) -> AsyncSession:
        async with self as db:
            yield db
    
    async def commit_rollback(self):
        try:
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise

db = DatabaseSession()