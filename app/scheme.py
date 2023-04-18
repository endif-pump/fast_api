# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
# pylint: disable=no-name-in-module

"""API contract schemes"""

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class Sex(Enum):
    MAN = "m"
    WOMEN = "w"


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
