from pydantic import BaseModel


class TokenData(BaseModel):
    email: str
    username: str
    role: str


class Token(BaseModel):
    access_token: str
    refresh_token: str
    info: TokenData
