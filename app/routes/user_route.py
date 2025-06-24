from fastapi import APIRouter, Response, status, Depends
from app.models.user_model import User
import app.services.user_service as user_service
from typing import Annotated

router = APIRouter(prefix="/users")

@router.post("/")
def create_user(user: User, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return user_service.create_user(user)

@router.get("/")
def get_users(response: Response):
    response.status_code = status.HTTP_200_OK
    return user_service.get_users()

@router.get("/{id}/projects")
def get_projects_by_user_id(id: str, response: Response, current_user: Annotated[User, Depends(user_service.get_current_user)]):
    response.status_code = status.HTTP_200_OK
    return user_service.get_projects_by_user_id(id)

@router.put("/{id}")
def update_user(id: str, user: User, response: Response, current_user: Annotated[User, Depends(user_service.get_current_user)]):
    result = user_service.update_user(id, user)
    if result.get("status") == 404: response.status_code = status.HTTP_404_NOT_FOUND
    elif result.get("status") == 200: response.status_code = status.HTTP_200_OK

    return result

router.delete("/{id}")
def delete_user(id: str, response: Response, current_user: Annotated[User, Depends(user_service.get_current_user)]):
    result = user_service.delete_user(id)
    if result.get("status") == 404: response.status_code = status.HTTP_404_NOT_FOUND
    elif result.get("status") == 200: response.status_code = status.HTTP_200_OK

    return result


