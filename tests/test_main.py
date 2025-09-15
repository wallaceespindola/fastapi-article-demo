from collections.abc import Generator
from http import HTTPStatus

from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

from app.database import get_session
from app.main import app

# Create a test database in memory
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# Create test database tables
SQLModel.metadata.create_all(engine)


# Override the dependencies with test versions
def override_get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


# Apply the dependency override
app.dependency_overrides[get_session] = override_get_session

# Setup test client with overrides
client = TestClient(app)


def test_root() -> None:
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello, FastAPI Article Project!"}


def test_create_user() -> None:
    response = client.post(
        "/users/",
        json={"name": "Test User", "email": "test@example.com", "password": "password123"},
    )
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"
    assert "id" in data


def test_background_task() -> None:
    response = client.post("/tasks/action/", params={"user": "testuser"})
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Action scheduled"}
