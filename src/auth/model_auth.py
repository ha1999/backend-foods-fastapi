from pydantic import BaseModel


class DataAuthLocal(BaseModel):
    username: str
    passwd: str
