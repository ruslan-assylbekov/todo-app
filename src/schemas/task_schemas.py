from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TaskCreate(BaseModel):
    user_id:     str
    text: str
    due_date: datetime | None = None


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:        int
    user_id:     str
    text: str
    due_date: datetime | None = None
    created:   datetime
    last_updated: datetime
