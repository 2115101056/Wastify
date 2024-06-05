from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    user_id: int
    username: str
    full_name: Optional[str] = None
    email: EmailStr
    password: str
