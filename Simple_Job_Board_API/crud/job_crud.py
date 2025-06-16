from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.job_model import Job
from schemas.job_schema import JobCreate, JobUpdate


async def create_job(db: AsyncSession, job_create: JobCreate):
    new_job= Job(
        title= job_create.title,
        description= job_create.description,
        company= job_create.company,
        location= job_create.location,
        salary= job_create.salary
    )
    db.add(new_job)
    await db.commit()
    await db.refresh(new_job)
    return new_job
    

async def update_job(job_id: int, db: AsyncSession, job_update: JobUpdate):
    existing_job= await db.get(Job,job_id)
    if not existing_job:
        return None
    
    if job_update.title is not None:
        existing_job.title= job_update.title
    if job_update.description is not None:
        existing_job.description= job_update.description
    if job_update.company is not None:
        existing_job.company= job_update.company
    if job_update.location is not None:
        existing_job.location= job_update.location
    if job_update.salary is not None:
        existing_job.salary= job_update.salary
    
        
    await db.commit()
    await db.refresh(existing_job)
    return existing_job

async def get_job_by_id(job_id: int, db: AsyncSession):
    job= await db.get(Job, job_id)
    return job

async def get_all_jobs(db: AsyncSession):
    result= await db.execute(select(Job))
    jobs= result.scalars().all()
    return jobs

async def delete_job(job_id: int, db: AsyncSession):
    job= await db.get(Job, job_id)
    if not job:
        return None
    await db.delete(job)
    await db.commit()
    return job
