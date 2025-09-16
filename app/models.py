from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):  # type: ignore[call-arg]
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str


class Item(SQLModel, table=True):  # type: ignore[call-arg]
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
