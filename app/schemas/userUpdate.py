from pydantic import BaseModel

class UserUpdate(BaseModel):
    email: str
    current_password: str
    username: str
    new_password: str
    is_active: bool = True