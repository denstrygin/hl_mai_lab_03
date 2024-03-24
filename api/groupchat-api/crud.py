from sqlalchemy.orm import Session
import models
import redis
import json

redis_conn = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

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
    redis_conn.delete(f"chat_members:{chat_id}")
    return new_member

def add_message_to_chat(db: Session, message: models.GroupChatMessage):
    db.add(message)
    db.commit()
    redis_conn.delete(f"chat_messages:{message.chat_id}")
    return message

def get_chat_messages(db: Session, chat_id: int):
    cache_key = f"chat_messages:{chat_id}"
    cached_messages = redis_conn.get(cache_key)
    if cached_messages:
        return json.loads(cached_messages)
    else:
        messages = db.query(models.GroupChatMessage).filter(models.GroupChatMessage.chat_id == chat_id).all()
        redis_conn.setex(cache_key, 60, json.dumps([message.as_dict() for message in messages]))  # Cache for 60 seconds
        return messages
