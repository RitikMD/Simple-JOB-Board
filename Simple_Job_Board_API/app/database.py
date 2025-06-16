import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

#loading the environment variables(database url) from .env file
load_dotenv()
DATABASE_URL= os.getenv("DATABASE_URL")

#it creates an asynchronous database engine to connect the database
engine= create_async_engine(DATABASE_URL, echo= True)

# sessionmaker for creating async sessions to perform database operations
AsyncSessionLocal= async_sessionmaker(bind= engine, expire_on_commit= False, class_= AsyncSession)

#it will get session for each request or operation with the database
async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session