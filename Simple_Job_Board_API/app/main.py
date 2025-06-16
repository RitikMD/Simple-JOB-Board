from fastapi import FastAPI
from api.job_routes import job_router


app= FastAPI(
    title= "SIMPLE JOB BOARD",
    description= "A simple job board API for posting and viewing job listings."
)


app.include_router(job_router)