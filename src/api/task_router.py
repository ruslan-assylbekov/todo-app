from fastapi import APIRouter
from src.schemas.task_schemas import TaskCreate, TaskResponse

router = APIRouter(prefix="/task", tags=["Tasks"])

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    pass
