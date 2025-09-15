from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

# SQLite URL
sqlite_url = "sqlite:///./test.db"
# Create engine
engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread": False})


# Create all tables
def create_tables() -> None:
    SQLModel.metadata.create_all(engine)


# Get session
def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
