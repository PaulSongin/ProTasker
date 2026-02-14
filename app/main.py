import os
from typing import List
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app import models, schemas, crud, utils
from app.database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ProTasker API",
    description="Full-stack Task Management System",
    version="1.0.0"
)

static_path = os.path.join("app", "static")
templates_path = os.path.join("app", "templates")

if not os.path.exists(static_path):
    os.makedirs(static_path)
if not os.path.exists(templates_path):
    os.makedirs(templates_path)

app.mount("/static", StaticFiles(directory=static_path), name="static")

templates = Jinja2Templates(directory=templates_path)



@app.get("/", response_class=HTMLResponse, tags=["Frontend"])
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    file_path = os.path.join(static_path, "favicon.ico")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"detail": "Not Found"}


@app.post("/register", response_model=schemas.User, status_code=status.HTTP_201_CREATED, tags=["Users"])
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    return crud.create_user(db=db, user=user)


@app.post("/users/{user_id}/tasks/", response_model=schemas.Task, status_code=status.HTTP_201_CREATED, tags=["Tasks"])
def create_task_for_user(user_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.create_task(db=db, task=task, user_id=user_id)


@app.get("/tasks/", response_model=List[schemas.Task], tags=["Tasks"])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tasks(db, skip=skip, limit=limit)


@app.get("/users/{user_id}/tasks/", response_model=List[schemas.Task], tags=["Tasks"])
def read_user_tasks(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_tasks(db, user_id=user_id)