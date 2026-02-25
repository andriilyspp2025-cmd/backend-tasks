from pydantic import BaseModel

class SignUpReq(BaseModel):
    email: str
    password: str
    username: str