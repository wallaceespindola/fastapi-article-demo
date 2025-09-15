from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app.auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    authenticate_user,
    create_access_token,
    get_current_user,
)
from app.database import get_session
from app.models import User

router = APIRouter()

# Define dependencies at module level
form_dependency = Depends(OAuth2PasswordRequestForm)
db_session = Depends(get_session)
current_user_dependency = Depends(get_current_user)


@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = form_dependency,
    session: Session = db_session,
) -> dict[str, str]:
    user = await authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = current_user_dependency) -> User:
    return current_user
