from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.project_route import router as project_router
from app.routes.user_route import router as user_router
from app.routes.task_route import router as task_router
from app.routes.auth_route import router as auth_router

app = FastAPI()

origins= [
    "http://localhost:8080",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/api")
app.include_router(project_router, prefix="/api")
app.include_router(task_router, prefix="/api")
app.include_router(auth_router, prefix="/api")
