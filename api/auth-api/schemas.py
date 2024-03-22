from pydantic import BaseModel

class UserCreate(BaseModel):
    login: str
    password: str
    first_name: str
    last_name: str
    email: str

class UserResponse(BaseModel):
    user_id: int
    login: str
    first_name: str
    last_name: str
    email: str

    class Config:
        from_attributes = True