# pylint: disable=relative-beyond-top-level

"""Main endpoint for app"""

from fastapi import FastAPI, Depends
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_users import fastapi_users, FastAPIUsers
from redis import asyncio as aioredis

from .database import User
from .auth.base_config import auth_backend
from .auth.schemas import UserRead, UserCreate
from .auth.manager import get_user_manager
from .operations.router import router as router_operation

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(
    title="Pet prj"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hi {user.email}"


app.include_router(router_operation)

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
