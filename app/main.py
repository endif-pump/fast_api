# pylint: disable=relative-beyond-top-level

"""Main endpoint for app"""

from typing import List

from fastapi import FastAPI

from .fake_db import FakeDB
from .scheme import Data, User

app = FastAPI(
    title="Pet prj"
)

db = FakeDB()


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    "Endpoints to get a specific user"

    return [user for user in db.fake_users if user.get("id") == user_id]


@app.get("/data")
def get_data(limit: int = 1, offset: int = 0):
    "Endpoints to get data"

    return db.fake_data[offset:][:limit]


@app.post("/data")
def add_data(data: List[Data]):
    "Endpoints to add data"

    db.fake_data.extend(data)

    return {"status": 200, "data":  db.fake_data}


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    "Endpoints to change isername for user"

    current_user = list(filter(lambda user: user.get("id")
                        == user_id, db.fake_users))[0]
    current_user['name'] = new_name

    return {"status": 200, "data": current_user}
