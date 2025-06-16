from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

Base= declarative_base()

class Job(Base):
    __tablename__= "jobs"

    id= Column(Integer, primary_key= True, autoincrement= True)
    title= Column(String(100), nullable= False)
    description= Column(String(500), nullable= False)
    company= Column(String(100), nullable= False)
    location= Column(String(100), nullable= False)
    salary= Column(Integer, nullable= True)
    posted_at= Column(DateTime, default= lambda: datetime.now(timezone.utc), nullable= False)
    updated_at= Column(DateTime, onupdate= lambda: datetime.now(timezone.utc), nullable= True)