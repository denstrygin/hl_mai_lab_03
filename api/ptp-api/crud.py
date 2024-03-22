from sqlalchemy.orm import Session
import models

def send_ptp_message(db: Session, message: models.PtpMessage):
    db.add(message)
    db.commit()
    return message

def get_ptp_messages(db: Session, user_id: int):
    return db.query(models.PtpMessage).filter((models.PtpMessage.sender_user_id == user_id) | (models.PtpMessage.recipient_user_id == user_id)).all()