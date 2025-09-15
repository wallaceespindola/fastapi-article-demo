from typing import cast

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models import User

router = APIRouter()

# Define dependencies at module level
db_session = Depends(get_session)


@router.post("/", response_model=User)
async def create_user(user: User, session: Session = db_session) -> User:
    # Check if user with the same email already exists
    statement = select(User).where(User.email == user.email)
    existing_user = session.exec(statement).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # Add new user
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int, session: Session = db_session) -> User:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return cast(User, user)
