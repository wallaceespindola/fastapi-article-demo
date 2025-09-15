from fastapi import APIRouter, HTTPException
from app.models import Item

router = APIRouter()
_fake_items = {}

@router.post("/", response_model=Item)
async def create_item(item: Item):
    if item.name in _fake_items:
        raise HTTPException(status_code=400, detail="Item already exists")
    _fake_items[item.name] = item
    return item

@router.get("/{name}", response_model=Item)
async def get_item(name: str):
    item = _fake_items.get(name)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
