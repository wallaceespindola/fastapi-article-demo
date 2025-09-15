import os
from collections.abc import Generator

from dotenv import load_dotenv
from sqlmodel import Session, SQLModel, create_engine, select

from app.models import Item, User

# Load environment variables
load_dotenv()

# Database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})


# Create all tables
def create_tables() -> None:
    SQLModel.metadata.create_all(engine)


# Get session
def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


# Load test data
def load_test_data() -> None:
    # Import here to avoid circular import
    from app.auth import get_password_hash  # noqa: PLC0415

    with Session(engine) as session:
        # Check if test data already exists
        existing_users = session.exec(select(User)).all()
        if existing_users:
            print("Test data already exists, skipping...")
            return

        # Create test users
        test_users = [
            User(
                name="John Doe", email="john@example.com", password=get_password_hash("password123")
            ),
            User(
                name="Jane Smith",
                email="jane@example.com",
                password=get_password_hash("password456"),
            ),
        ]

        # Create test items
        test_items = [
            Item(
                name="Laptop",
                description="High-performance laptop for development",
                price=1299.99,
                tax=119.99,
            ),
            Item(
                name="Wireless Mouse",
                description="Ergonomic wireless mouse with precision tracking",
                price=49.99,
                tax=4.50,
            ),
        ]

        # Add test data to session
        for user in test_users:
            session.add(user)

        for item in test_items:
            session.add(item)

        session.commit()
        print("Test data loaded successfully!")
