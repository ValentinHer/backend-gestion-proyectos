from pydantic import BaseModel
from enum import Enum

class StateProject(str, Enum):
    pendiente = "pendiente"
    en_curso = "en curso"
    completado = "completado"

class Project(BaseModel):
    nombre: str
    descripcion: str | None = None
    estado: StateProject | None = StateProject.pendiente
    user_id: str | None = None

