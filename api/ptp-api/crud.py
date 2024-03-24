from sqlalchemy.orm import Session
import models
import redis
import json

redis_conn = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

def send_ptp_message(db: Session, message: models.PtpMessage):
    db.add(message)
    db.commit()
    redis_conn.delete(f"ptp_messages:{message.sender_user_id}")
    redis_conn.delete(f"ptp_messages:{message.recipient_user_id}")
    return message

def get_ptp_messages(db: Session, user_id: int):
    cache_key = f"ptp_messages:{user_id}"
    cached_messages = redis_conn.get(cache_key)
    if cached_messages:
        return json.loads(cached_messages)
    else:
        messages = db.query(models.PtpMessage).filter(
            (models.PtpMessage.sender_user_id == user_id) | 
            (models.PtpMessage.recipient_user_id == user_id)
        ).all()
        redis_conn.setex(cache_key, 60, json.dumps([message.as_dict() for message in messages]))
        return messages