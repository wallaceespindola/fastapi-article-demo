from fastapi import APIRouter, HTTPException
from app.models import User

router = APIRouter()
_fake_users = {}

@router.post("/", response_model=User)
async def create_user(user: User):
    if user.email in _fake_users:
        raise HTTPException(status_code=400, detail="User already exists")
    _fake_users[user.email] = user
    return user

@router.get("/{email}", response_model=User)
async def get_user(email: str):
    user = _fake_users.get(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
