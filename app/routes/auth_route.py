from fastapi import APIRouter, status, Response, Depends
from app.services.auth_service import user_login
from app.models.auth_model import LoginModel
from app.services.user_service import get_current_user
from typing import Annotated
from app.models.user_model import User
 
router = APIRouter(prefix="/auth")

@router.post("/login")
def login(login: LoginModel, response: Response):
    token = user_login(login)
    response.set_cookie(key="token", value=token, httponly=True, secure=False, path="/", samesite="lax")
    # Establecer la cookie manualmente con Partitioned
    # response.headers["Set-Cookie"] = (
    #     f"token={token}; Path=/; HttpOnly; SameSite=Lax; Partitioned"
    # )    
    response.status_code = status.HTTP_200_OK
    return {"message": "Login Exitoso", "status": status.HTTP_200_OK}

@router.get("/check")
def check_auth(current_user: Annotated[User, Depends(get_current_user)], response: Response):
    if current_user:
        response.status_code = status.HTTP_200_OK
        return {"message": "Usuario autenticado", "status": status.HTTP_200_OK}
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return {"message": "Usuario no autenticado", "status": status.HTTP_401_UNAUTHORIZED}

@router.get("/logout")
def logout(current_user: Annotated[User, Depends(get_current_user)], response: Response):
    response.status_code = status.HTTP_200_OK
    response.delete_cookie("token")
    return {"message": "Sesión terminado", "status": status.HTTP_200_OK}
