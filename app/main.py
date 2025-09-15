from fastapi import FastAPI

from app.database import create_tables
from app.routes import auth, background_tasks, items, users

app = FastAPI(title="FastAPI Article Demo")
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(auth.router, tags=["Authentication"])
app.include_router(background_tasks.router, prefix="/tasks", tags=["Background Tasks"])


@app.on_event("startup")
def on_startup() -> None:
    create_tables()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello, FastAPI Article Project!"}
