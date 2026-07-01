from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TaskCreate(BaseModel):
    text: str
    due_date: datetime | None = None


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:        int
    user_id: int
    text: str
    due_date: datetime | None = None
    created:   datetime
    last_updated: datetime
