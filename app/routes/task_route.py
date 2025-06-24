from fastapi import APIRouter, Response, status, Depends
from app.models.task_model import Task 
import app.services.task_service as task_service
from typing import Annotated
from app.models.user_model import User
from app.services.user_service import get_current_user

router = APIRouter(prefix="/tasks")

@router.post("/")
def create_task(task: Task, response: Response, current_user: Annotated[User, Depends(get_current_user)]):
    response.status_code = status.HTTP_201_CREATED
    return task_service.create_task(task)

@router.put("/{id}")
def update_task(id: str, task: Task, response: Response, current_user: Annotated[User, Depends(get_current_user)]):
    result = task_service.update_task(id, task)

    if result.get("status") == 404:
        response.status_code = status.HTTP_404_NOT_FOUND
    elif result.get("status") == 200:
        response.status_code = status.HTTP_200_OK

    return result
    

@router.delete("/{id}")
def delete_task(id: str, response: Response, current_user: Annotated[User, Depends(get_current_user)]):
    result = task_service.delete_task(id)

    if result.get("status") == 404: 
        response.status_code = status.HTTP_404_NOT_FOUND
    elif result.get("status") == 200:
        response.status_code = status.HTTP_200_OK
        
    return result