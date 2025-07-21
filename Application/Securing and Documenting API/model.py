from pydantic import BaseModel
class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str
    full_name: str

class Login(BaseModel):
    username: str
    password: str