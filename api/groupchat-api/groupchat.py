from fastapi import FastAPI, Depends, HTTPException
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

@app.post("/create_group_chat/", response_model=schemas.GroupChatResponse)
def create_group_chat(chat: schemas.GroupChatCreate, db: Session = Depends(get_db)):
    db_chat = crud.create_group_chat(db, models.GroupChat(chat_name=chat.chat_name, creator_user_id=chat.creator_user_id), chat.member_user_ids)
    return db_chat

@app.post("/add_user_to_chat/")
def add_user_to_chat(data: schemas.AddUserToChat, db: Session = Depends(get_db)):
    db_member = crud.add_user_to_chat(db, data.chat_id, data.user_id)
    return {"message": "User added to chat successfully"}

@app.post("/add_message_to_chat/")
def add_message_to_chat(message: schemas.GroupChatMessageCreate, db: Session = Depends(get_db)):
    db_message = crud.add_message_to_chat(db, models.GroupChatMessage(**message.dict()))
    return {"message": "Message added to chat successfully"}

@app.get("/get_chat_messages/", response_model=List[schemas.GroupChatMessageResponse])
def get_chat_messages(chat_id: int, db: Session = Depends(get_db)):
    db_messages = crud.get_chat_messages(db, chat_id)
    return db_messages