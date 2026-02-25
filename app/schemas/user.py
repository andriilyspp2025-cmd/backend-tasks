from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

