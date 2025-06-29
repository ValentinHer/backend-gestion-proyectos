from fastapi import status
from app.models.project_model import Project
from app.database.db import db
from bson import ObjectId

def create_project(project: Project):
    project_dict = project.model_dump()

    project_dict["user_id"] = ObjectId(project.user_id)
    result = db.projects.insert_one(project_dict)
    return {"message": "Proyecto Creado Exitosamente", "status": status.HTTP_201_CREATED}

def get_tasks_by_project_id(project_id: str):
    result = db.tasks.find({"project_id": ObjectId(project_id)})
    tasks = []
    for task in result:
        task["_id"] = str(task["_id"])
        if "usuario_asignado" in task:
            task["usuario_asignado"] = str(task["usuario_asignado"])
        task["project_id"] = str(task["project_id"])
        tasks.append(task)
    return {"data": tasks, "status": status.HTTP_200_OK}

def update_project(project_id: str, project: Project, user_id: str):
    project_dict = project.model_dump()
    project_dict["user_id"] = ObjectId(user_id)

    result = db.projects.update_one(
        {"_id": ObjectId(project_id)},
        {"$set": project_dict}
    )
    if result.matched_count == 0: return {"message": "Proyecto No Encontrado", "status": status.HTTP_404_NOT_FOUND}

    return {"message": "Proyecto Actualizado Exitosamente", "status": status.HTTP_200_OK}

def delete_project(project_id: str):
    result = db.projects.delete_one({"_id": ObjectId(project_id)})
    if result.deleted_count == 0: return {"message": "Proyecto No Encontrado", "status": status.HTTP_404_NOT_FOUND}

    return {"message": "Proyecto Eliminado Exitosamente", "status": status.HTTP_200_OK}