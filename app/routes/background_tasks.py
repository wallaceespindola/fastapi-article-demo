from fastapi import APIRouter, BackgroundTasks
from typing import Dict

router = APIRouter()

def log_action(user: str):
    with open("audit.log", "a") as f:
        f.write(f"User {user} performed an action\n")

@router.post("/action/")
async def perform_action(user: str, background_tasks: BackgroundTasks) -> Dict[str, str]:
    background_tasks.add_task(log_action, user)
    return {"message": "Action scheduled"}
