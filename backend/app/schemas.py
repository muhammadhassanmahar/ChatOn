from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RegisterSchema(BaseModel):
    firebase_uid: str
    email: Optional[str] = None
    phone: Optional[str] = None
    username: Optional[str] = None
    photoUrl: Optional[str] = None
    bio: Optional[str] = None

class MessageCreateSchema(BaseModel):
    sender: str
    receiver: str
    text: str
    timestamp: Optional[datetime] = None
