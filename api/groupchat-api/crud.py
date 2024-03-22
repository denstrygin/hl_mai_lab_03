from sqlalchemy.orm import Session
import models

def create_group_chat(db: Session, chat: models.GroupChat, member_user_ids: list[int]):
    db.add(chat)
    db.commit()
    db.refresh(chat)
    for user_id in member_user_ids:
        new_member = models.GroupChatMember(chat_id=chat.chat_id, user_id=user_id)
        db.add(new_member)
    db.commit()
    return {"chat_id": chat.chat_id, "chat_name": chat.chat_name, "creator_user_id": chat.creator_user_id}

def add_user_to_chat(db: Session, chat_id: int, user_id: int):
    new_member = models.GroupChatMember(chat_id=chat_id, user_id=user_id)
    db.add(new_member)
    db.commit()
    return new_member

def add_message_to_chat(db: Session, message: models.GroupChatMessage):
    db.add(message)
    db.commit()
    return message

def get_chat_messages(db: Session, chat_id: int):
    return db.query(models.GroupChatMessage).filter(models.GroupChatMessage.chat_id == chat_id).all()