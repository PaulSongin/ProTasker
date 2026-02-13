from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    is_completed: bool
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True



class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    tasks: List[Task] = []

    class Config:
        from_attributes = True