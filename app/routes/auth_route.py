from fastapi import APIRouter, status, Response
from app.services.auth_service import user_login
from app.models.auth_model import LoginModel
 
router = APIRouter(prefix="/auth")

@router.post("/login")
def login(login: LoginModel, response: Response):
    token = user_login(login)
    response.set_cookie(key="token", value=token, httponly=True, secure=False)
    response.status_code = status.HTTP_200_OK
    return {"message": "Login Exitoso", "status": status.HTTP_200_OK}
