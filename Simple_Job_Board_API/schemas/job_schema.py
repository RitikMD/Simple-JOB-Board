from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class JobCreate(BaseModel):
    title: str= Field(..., min_length= 1, max_length= 100)
    description: str= Field(..., min_length= 1, max_length= 500)
    company: str= Field(..., min_length= 1, max_length= 100)
    location: str= Field(..., min_length= 1, max_length= 100)
    salary: Optional[int]= None
    
    class Config:
        form_attributes= True
        json_schema_extra= {
            "example":{
                "title": "Software Engineer",
                "description": "Develop and maintain software applications.",
                "company": "Tech Solutions Inc.",
                "location": "New York, NY",
                "salary": 500000
            }
        }
    
    
class JobUpdate(BaseModel):
    title: Optional[str]= Field(None, min_length= 1, max_length= 100)
    description: Optional[str]= Field(None, min_length= 1, max_length= 500)
    company: Optional[str]= Field(None, min_length= 1, max_length= 100)
    location: Optional[str]= Field(None, min_length= 1, max_length= 100)
    salary: Optional[int]= None
    
    class Config:
        form_attributes= True
        json_schema_extra= {
            "example":{
                "title": "Senior Software Engineer",
                "description": "Lead software development projects.",
                "company": "Tech Solutions Inc.",
                "location": "San Francisco, CA",
                "salary": 1000000
            }
        }

class JobGet(BaseModel):
    id: int
    title: str
    description: str
    company: str
    location: str
    salary: Optional[int]
    posted_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        form_attributes= True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Software Engineer",
                "description": "Develop and maintain software applications.",
                "company": "Tech Solutions Inc.",
                "location": "New York, NY",
                "salary": 500000,
                "posted_at": "2023-10-01T12:00:00Z",
                "updated_at": "2023-10-01T12:00:00Z"
            }
        }