from pydantic import BaseModel
from enum import Enum

class StateTask(str, Enum):
    pendiente = "pendiente"
    en_curso = "en curso"
    completado = "completado"

class PriorityTask(str, Enum):
    baja = "baja"
    media = "media"
    alta = "alta"
    urgente = "urgente"

class DifficultTask(str, Enum):
    baja = "baja"
    media = "media"
    alta = "alta"

class Task(BaseModel):
    descripcion: str | None = None
    usuario_asignado: str | None = None
    estado: StateTask | None = StateTask.pendiente
    prioridad: PriorityTask | None = PriorityTask.baja
    dificultad: DifficultTask | None = DifficultTask.baja
    vencimiento: str
    project_id: str