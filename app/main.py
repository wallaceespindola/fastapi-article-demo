from fastapi import FastAPI
from app.routes import users, items

app = FastAPI(title="FastAPI Article Demo")
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI Article Project!"}
