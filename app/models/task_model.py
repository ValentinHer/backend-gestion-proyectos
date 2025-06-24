from pydantic import BaseModel
from enum import Enum

class StateTask(str, Enum):
    pendiente = "Pendiente"
    en_curso = "En curso"
    completado = "Completado"

class Task(BaseModel):    
    nombre: str
    titulo: str
    descripcion: str | None = None
    usuario_asignado: str | None = None
    estado: StateTask = StateTask.pendiente
    project_id: str