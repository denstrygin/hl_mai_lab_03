from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, models, schemas
from models import SessionLocal
from typing import List

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/send_ptp_message/", response_model=schemas.PtpMessageResponse)
def send_ptp_message(message: schemas.PtpMessageCreate, db: Session = Depends(get_db)):
    db_message = crud.send_ptp_message(db, models.PtpMessage(**message.dict()))
    return db_message

@app.get("/get_ptp_messages/", response_model=List[schemas.PtpMessageResponse])
def get_ptp_messages(user_id: int, db: Session = Depends(get_db)):
    db_messages = crud.get_ptp_messages(db, user_id)
    return db_messages