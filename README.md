# Backend: Gestión de Proyectos

## Descripción
Backend de una aplicación de gestión de proyectos, usando Python con [FastAPI](https://fastapi.tiangolo.com/) y [MongoDB](https://www.mongodb.com/) para la persistencia de datos.

- Clona o descarga el repositorio.

## Configuración
- Crea un entorno virtual (esto para que las dependencias no se instalen globalmente) ejecutando el siguiente comando:

    ```
    python -m venv .venv
    ```
- Una vez creado el entorno virtual procede a activarlo con el siguiente comando:

    ```
    .venv\Scripts\Activate.ps1
    ```

- Para checar si esta activado ejecuta el siguiente comando:

    ```
    Get-Command python
    ```
    - Esto tiene que mostra algo similar a lo siguiente:
    `C:\Users\user\code\awesome-project\.venv\Scripts\python`

- Si todo salió bien, entonces ahora crea un archivo `.gitignore` dentro de la carpeta `.venv`, esto para que no se suba nada de lo que contenga la carpeta, puedes usar el siguiente comando:
    ```
    echo "*" > .venv/.gitignore
    ```

- Una vez finalizado el uso de la APIRest, desactiva el entorno virtual con el siguiente comando:

    ```
    deactivate
    ```

## Instalación
- Instala las dependencias del proyecto con el siguiente comando:
    ```
    pip install -r requirements.txt
    ```

## Inicialización
- Ejecuta el proyecto usando el siguiente comando:

    ```
    fastapi dev app/main.py
    ``` 
    o 
    ```
    uvicorn app.main:app --reload --host localhost --port 8000
    ```