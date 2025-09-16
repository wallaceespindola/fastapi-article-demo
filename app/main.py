from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import create_tables, load_test_data
from app.routes import auth, background_tasks, items, users


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # Startup
    create_tables()
    load_test_data()
    yield
    # Shutdown (if needed)


app = FastAPI(title="FastAPI Article Demo", lifespan=lifespan)
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(auth.router, tags=["Authentication"])
app.include_router(background_tasks.router, prefix="/tasks", tags=["Background Tasks"])


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello, FastAPI Demo Project!"}
