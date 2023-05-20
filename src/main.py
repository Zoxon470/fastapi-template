from fastapi import FastAPI
from config import settings
from example.routes import router as example_router

app = FastAPI(
    title=settings.SERVICE_NAME,
)


app.include_router(
    example_router,
    tags=["example"]
)
