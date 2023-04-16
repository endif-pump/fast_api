from typing import List

from fastapi import FastAPI

from .fake_db import Fake_DB
from .scheme import Data, User

app = FastAPI(
    title="Pet prj"
)

db = Fake_DB

@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in db.fake_users if user.get("id") == user_id]

@app.get("/data")
def get_data(limit: int = 1, offset: int = 0):
    return db.fake_data[offset:][:limit]

@app.post("/data")
def add_data(data: List[Data]):
    db.fake_data.extend(data)
    return {"status": 200, "data":  db.fake_data}

@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, db.fake_users))[0]
    print(current_user)
    current_user['name'] = new_name
    return {"status": 200, "data": current_user}