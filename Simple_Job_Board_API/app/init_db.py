import asyncio
from app.database import engine
from models.job_model import Job

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Job.metadata.create_all)
    print("Database initialized and tables created.")
    
if __name__== "__main__":
    asyncio.run(init_db())