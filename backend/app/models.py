from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserModel(BaseModel):
    firebase_uid: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    username: Optional[str] = None
    photoUrl: Optional[str] = None
    bio: Optional[str] = None
    created_at: datetime = datetime.utcnow()

class MessageModel(BaseModel):
    sender: str
    receiver: str
    text: str
    timestamp: datetime = datetime.utcnow()
    delivered: bool = False
    read: bool = False
