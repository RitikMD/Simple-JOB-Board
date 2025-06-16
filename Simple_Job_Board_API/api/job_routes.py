from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from schemas.job_schema import JobCreate, JobUpdate, JobGet
from crud.job_crud import create_job, update_job, get_job_by_id, get_all_jobs, delete_job
from typing import List


job_router= APIRouter(tags= ["JOBS"])

@job_router.post("/jobs", response_model= JobGet, status_code= status.HTTP_201_CREATED)
async def create_new_job(job_create: JobCreate, db: AsyncSession= Depends(get_async_session)):
    job= await create_job(db, job_create)
    return job

@job_router.put("/jobs/{job_id}", response_model= JobGet, status_code= status.HTTP_200_OK)
async def update_existing_job(job_id: int, job_update: JobUpdate, db: AsyncSession= Depends(get_async_session)):
    updated_job= await update_job(job_id, db, job_update)
    if not updated_job:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Job with id {job_id} not found")
    return updated_job


@job_router.get("/jobs/{job_id}", response_model= JobGet, status_code= status.HTTP_200_OK)
async def get_job(job_id: int, db: AsyncSession= Depends(get_async_session)):
    job= await get_job_by_id(job_id, db)
    if not job:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Job with id {job_id} not found")
    return job


@job_router.get("/jobs", response_model= List[JobGet], status_code= status.HTTP_200_OK)
async def get_all_jobs_list(db: AsyncSession= Depends(get_async_session)):
    jobs= await get_all_jobs(db)
    return jobs

@job_router.delete("/jobs/{job_id}", response_model= JobGet, status_code= status.HTTP_200_OK)
async def delete_existing_job(job_id: int, db: AsyncSession= Depends(get_async_session)):
    deleted_job= await delete_job(job_id, db)
    if not deleted_job:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Job with id {job_id} not found")
    return deleted_job

