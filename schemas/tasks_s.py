from pydantic import BaseModel


class CreateTask(BaseModel):
    title: str
    description: str | None = None
    
    
class TaskInfo(CreateTask):
    id: int
    
    class Config:
        orm_mode = True
        

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None