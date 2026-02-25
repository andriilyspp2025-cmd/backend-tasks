from pydantic import BaseModel, ConfigDict

class UserDetailRes(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
