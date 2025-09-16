"""Security utilities for password hashing and verification."""

from typing import cast

from dotenv import load_dotenv
from passlib.context import CryptContext

# Load environment variables
load_dotenv()

# Password context for hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password."""
    result = pwd_context.verify(plain_password, hashed_password)
    return cast(bool, result)


def get_password_hash(password: str) -> str:
    """Generate a hash for a password."""
    result = pwd_context.hash(password)
    return cast(str, result)
