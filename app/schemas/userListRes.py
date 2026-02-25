from pydantic import BaseModel
from typing import List
from app.schemas.userDetailRes import UserDetailRes

class UserListRes(BaseModel):
    users: List[UserDetailRes]