from typing import cast

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models import Item

router = APIRouter()

# Define dependencies at module level
db_session = Depends(get_session)


@router.post("/", response_model=Item)
async def create_item(item: Item, session: Session = db_session) -> Item:
    # Check if item with the same name already exists
    statement = select(Item).where(Item.name == item.name)
    existing_item = session.exec(statement).first()
    if existing_item:
        raise HTTPException(status_code=400, detail="Item already exists")

    # Add new item
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int, session: Session = db_session) -> Item:
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return cast(Item, item)
