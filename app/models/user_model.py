from pydantic import BaseModel

class User(BaseModel):
    nombre: str
    apellidos: str
    email: str
    contrasenia: str

