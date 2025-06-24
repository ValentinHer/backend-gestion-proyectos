from fastapi import status, Depends, HTTPException
from app.database.db import db
from app.models.user_model import User
from bson import ObjectId
from app.utils.password_util import get_password_hash, valid_password
from typing import Annotated
from app.utils.token_util import get_token_from_cookie
from app.utils.jwt_util import valid_jwt

def create_user(user: User):
    user_found = db.users.find_one({"email": user.email})
    if user_found : raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El email ya se encuentra registrado")

    user_dict = user.model_dump()
    user_dict['contrasenia'] = get_password_hash(user.contrasenia)

    result = db.users.insert_one(user_dict)
    return {"message": "Usuario Creado Exitosamente", "status": status.HTTP_201_CREATED}

def get_users():
    results = db.users.find()
    users = []
    for user in results:
        user["_id"] = str(user["_id"])  # Convertir ObjectId a str
        users.append(user)
    return {"data": users, "status": status.HTTP_200_OK}

def get_projects_by_user_id(user_id: str):
    results = db.projects.find({"user_id": ObjectId(user_id)})
    projects = []
    for project in results:
        project["_id"] = str(project["_id"])
        project["user_id"] = str(project["user_id"])
        projects.append(project)
    return {"data": projects, "status": status.HTTP_200_OK}

def get_user_by_email(email: str, password: str):
    user_found = db.users.find_one({"email": email})
    if not user_found: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Revice sus credenciales, inténtelo de nuevo")
    
    if not valid_password(password, user_found["contrasenia"]): raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Revice sus credenciales, inténtelo de nuevo")

    user_found["_id"] = str(user_found["_id"])
    return user_found

def get_one_user_by_email(email: str):
    user_found = db.users.find_one({"email": email})
    if not user_found: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario No Encontrado")
    
    user_found["_id"] = str(user_found["_id"])
    return user_found

def update_user(user_id: str, user: User):
    result = db.users.update_one({"_id": ObjectId(user_id)}, user)
    if result.matched_count == 0: return {"message": "Usuario No Encontrado", "status": status.HTTP_404_NOT_FOUND}

    return {"message": "Usuario Actualizado Exitosamente", "status": status.HTTP_200_OK}

def delete_user(user_id: str):
    result = db.users.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0: return {"message": "Usuario No Encontrado", "status": status.HTTP_404_NOT_FOUND}
    
    return {"message": "Usuario Eliminado Exitosamente", "status": status.HTTP_200_OK}

def get_current_user(token: Annotated[str, Depends(get_token_from_cookie)]):
    payload = valid_jwt(token)
    user_email = payload.get("sub")

    if user_email is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    
    user = get_one_user_by_email(user_email)

    user["_id"] = str(user["_id"])
    return user