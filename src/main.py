import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.config import settings
from src.example.routes import router as example_router
from src.user.auth import auth_backend
from src.user.manager import get_user_manager
from src.user.models import User
from src.user.schemas import UserRead, UserCreate

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)


app = FastAPI(
    title=settings.SERVICE_NAME,
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

app.include_router(
    example_router,
    tags=["example"]
)
