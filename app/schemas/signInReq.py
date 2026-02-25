from pydantic import BaseModel

class SignInReq(BaseModel):
    email: str
    password: str