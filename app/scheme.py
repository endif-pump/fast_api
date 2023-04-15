from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class Sex(Enum):
    m = "m"
    w = "w"

class Info(BaseModel):
    sex: Sex
    old: int

class Data(BaseModel):
    id: int = Field(ge=0)
    count: int = Field(ge=0)
    money: int = Field(ge=0)
    
class User(BaseModel):
    id: int
    name: str
    info: Optional[List[Info]] = []