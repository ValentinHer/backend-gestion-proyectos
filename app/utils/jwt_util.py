from fastapi import HTTPException
from datetime import datetime, timedelta, timezone
import jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa12k342kjb4k24"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_jwt(data: dict, expires_token: timedelta | None = None):
    data_encode = data.copy()
    if expires_token:
        expire = datetime.now(timezone.utc) + expires_token
    else:
        expire = datetime.now(timezone.utc) + timedelta(hours=1)
    data_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(data_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def valid_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Token inválido")