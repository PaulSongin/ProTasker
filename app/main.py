from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ProTasker API")

@app.get("/")
def read_root():
    return {"message": "Welcome to ProTasker API", "docs": "/docs"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

