from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email:     EmailStr
    password:  str
    firstname: str
    lastname:  str

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:        int
    password: str
    email:     str
    firstname: str
    lastname:  str
    created:   datetime
    last_updated: datetime

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = None
    firstname: str | None = None
    lastname: str | None = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str
