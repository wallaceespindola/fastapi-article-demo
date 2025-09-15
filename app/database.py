from sqlmodel import create_engine, SQLModel, Session

# SQLite URL
sqlite_url = "sqlite:///./test.db"
# Create engine
engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread": False})

# Create all tables
def create_tables():
    SQLModel.metadata.create_all(engine)

# Get session
def get_session():
    with Session(engine) as session:
        yield session
