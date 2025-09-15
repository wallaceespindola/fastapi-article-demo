from fastapi.testclient import TestClient
from fastapi import Depends
from app.main import app
from sqlmodel import Session, SQLModel, create_engine
from sqlalchemy.pool import StaticPool
from app.models import User, Item
from app.database import get_session

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
def override_get_session():
    with Session(engine) as session:
        yield session

# Apply the dependency override
app.dependency_overrides[get_session] = override_get_session

# Setup test client with overrides
client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI Article Project!"}

def test_create_user():
    response = client.post(
        "/users/",
        json={"name": "Test User", "email": "test@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_background_task():
    response = client.post("/tasks/action/", params={"user": "testuser"})
    assert response.status_code == 200
    assert response.json() == {"message": "Action scheduled"}
