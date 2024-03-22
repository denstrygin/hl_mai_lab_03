from pydantic import BaseModel
from typing import List
from datetime import datetime

class PtpMessageCreate(BaseModel):
    sender_user_id: int
    recipient_user_id: int
    message_content: str

class PtpMessageResponse(BaseModel):
    message_id: int
    sender_user_id: int
    recipient_user_id: int
    message_content: str
    timestamp: datetime