from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.models import User
from app.database import get_session

router = APIRouter()

@router.post("/", response_model=User)
async def create_user(user: User, session: Session = Depends(get_session)):
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
async def get_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
