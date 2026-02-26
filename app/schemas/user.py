from pydantic import BaseModel, ConfigDict
from typing import List
from uuid import UUID
from datetime import datetime

class SignInReq(BaseModel):
    email: str
    password: str

class SignUpReq(BaseModel):
    email: str
    password: str
    username: str

class User(BaseModel):
    id: UUID
    email: str
    username: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserDetailRes(BaseModel):
    id: UUID
    email: str
    username: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserListRes(BaseModel):
    users: List[UserDetailRes]

class UserUpdate(BaseModel):
    email: str
    current_password: str
    username: str
    new_password: str
    is_active: bool = True
