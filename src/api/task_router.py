from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.database import get_session
from src.core.security import get_current_user
from src.models.database_models import tasks, users
from src.schemas.task_schemas import TaskCreate, TaskResponse

router = APIRouter(prefix="/task", tags=["Tasks"])

@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_session),
    current_user: users = Depends(get_current_user),
):
    new_task = tasks(**task.model_dump(), user_id=current_user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
