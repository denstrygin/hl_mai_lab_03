from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class GroupChatCreate(BaseModel):
    chat_name: str
    creator_user_id: int
    member_user_ids: List[int]

class AddUserToChat(BaseModel):
    chat_id: int
    user_id: int

class GroupChatMemberAdd(BaseModel):
    chat_id: int
    user_id: int

class GroupChatMessageCreate(BaseModel):
    chat_id: int
    sender_user_id: int
    message_content: str
    
class GroupChatResponse(BaseModel):
    chat_id: int
    chat_name: str
    creator_user_id: int

class GroupChatMessageResponse(BaseModel):
    message_id: int
    chat_id: int
    sender_user_id: int
    message_content: str
    timestamp: datetime

    class Config:
        from_attributes = True