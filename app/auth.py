from datetime import datetime, timedelta
from typing import Any, cast

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlmodel import Session, select

from app.database import get_session
from app.models import User

# Security constants
SECRET_KEY = "your-secret-key-should-be-kept-secure"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password context for hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme for token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define dependencies at module level
token_dependency = Depends(oauth2_scheme)
db_session = Depends(get_session)


# Verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    result = pwd_context.verify(plain_password, hashed_password)
    return cast(bool, result)


# Get password hash
def get_password_hash(password: str) -> str:
    result = pwd_context.hash(password)
    return cast(str, result)


# Authenticate user
async def authenticate_user(email: str, password: str, session: Session) -> User | None:
    statement = select(User).where(User.email == email)
    user = session.exec(statement).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return cast(User, user)


# Create access token
def create_access_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return cast(str, encoded_jwt)


# Get current user
async def get_current_user(token: str = token_dependency, session: Session = db_session) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Fix the type error by checking before assigning
        sub_claim = payload.get("sub")
        if sub_claim is None:
            raise credentials_exception
        email: str = cast(str, sub_claim)
    except JWTError as e:
        raise credentials_exception from e

    statement = select(User).where(User.email == email)
    user = session.exec(statement).first()
    if user is None:
        raise credentials_exception
    return cast(User, user)
