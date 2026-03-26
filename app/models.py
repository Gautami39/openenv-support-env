from pydantic import BaseModel

class ResetRequest(BaseModel):
    task_id: str

class Action(BaseModel):
    action_type: str
    message: str