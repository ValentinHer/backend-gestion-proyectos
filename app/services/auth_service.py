from app.models.auth_model import LoginModel
from app.services.user_service import get_user_by_email
from app.utils.jwt_util import create_jwt
from datetime import timedelta

def user_login(login: LoginModel):
    user = get_user_by_email(email=login.email, password=login.password)

    access_token_expires = timedelta(hours=1)
    token = create_jwt(data={"sub": user["email"]}, expires_token=access_token_expires)
    return token