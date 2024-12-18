from enum import Enum
from pydantic import BaseModel

class TaskStatus(str, Enum):
    pendente = "pendente"
    em_progresso = "em_progresso"
    completada = "completada"

class TaskCreate(BaseModel):
    title: str
    description: str
    status: TaskStatus = TaskStatus.pendente

class TaskUpdate(BaseModel):
    title: str
    description: str
    status: TaskStatus