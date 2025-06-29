from fastapi import APIRouter, Response, status, Depends
from app.models.project_model import Project
from app.models.user_model import User
import app.services.project_service as project_service
from typing import Annotated
from app.services.user_service import get_current_user

router = APIRouter(prefix="/projects")

@router.post("/")
def create_project(project: Project, response: Response, current_user: Annotated[User, Depends(get_current_user)]):
    project.user_id = current_user["_id"]
    response.status_code = status.HTTP_201_CREATED
    return project_service.create_project(project)

@router.get("/{id}/tasks")
def get_tasks_by_project_id(id: str, current_user: Annotated[User, Depends(get_current_user)]):
    return project_service.get_tasks_by_project_id(id)

@router.put("/{id}")
def update_project(id: str, project: Project, response: Response, current_user: Annotated[User, Depends(get_current_user)]):
    user_id = current_user["_id"]
    result = project_service.update_project(id, project, user_id)
    if result.get("status") == 404: response.status_code = status.HTTP_404_NOT_FOUND
    elif result.get("status") == 200: response.status_code = status.HTTP_200_OK

    return result

@router.delete("/{id}")
def delete_project(id: str, response: Response, current_user: Annotated[User, Depends(get_current_user)]):
    result = project_service.delete_project(id)
    if result.get("status") == 404: response.status_code = status.HTTP_404_NOT_FOUND
    elif result.get("status") == 200: response.status_code = status.HTTP_200_OK
    
    return result