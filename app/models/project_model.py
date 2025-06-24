from pydantic import BaseModel

class Project(BaseModel):
    nombre: str
    descripcion: str | None = None
    user_id: str

