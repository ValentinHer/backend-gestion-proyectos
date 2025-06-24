from fastapi import status
from app.database.db import db
from app.models.task_model import Task
from bson import ObjectId

def create_task(task: Task):
    task_dict = task.model_dump()
    if task.usuario_asignado is not None:
        task_dict["usuario_asignado"] = ObjectId(task.usuario_asignado)
    task_dict["project_id"] = ObjectId(task.project_id)
    result = db.tasks.insert_one(task_dict)
    return {"message": "Tarea Creada Exitosamente", "status": status.HTTP_201_CREATED}

def update_task(task_id: str, task: Task):
    result = db.tasks.update_one({"_id": ObjectId(task_id)}, task)
    if result.matched_count == 0: return {"message": "Tarea No Encontrada", "status": status.HTTP_404_NOT_FOUND}
 
    return {"message": "Tarea Actualizada Exitosamente", "status": status.HTTP_200_OK}

def delete_task(task_id: str):
    result = db.tasks.delete_one({"_id", ObjectId(task_id)})
    if result.deleted_count == 0: return {"message": "Tarea No Encontrada","status": status.HTTP_404_NOT_FOUND}

    return {"message": "Tarea Eliminada Exitosamente", "status": status.HTTP_200_OK}