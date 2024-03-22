from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas

app = FastAPI()

def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_user/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, models.User(**user.dict()))
    return db_user

@app.get("/get_user_by_login/", response_model=schemas.UserResponse)
def get_user_by_login(login: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_login(db, login)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/search_users/", response_model=list[schemas.UserResponse])
def search_users(first_name_mask: str = None, last_name_mask: str = None, db: Session = Depends(get_db)):
    users = crud.search_users(db, first_name_mask, last_name_mask)
    return users