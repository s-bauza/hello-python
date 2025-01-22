from fastapi import Depends, status, APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1  # 1 minute
SECRET = "0d76d27c423258154a492ec996167e5b6e214666b70b4e49df358e8e39b4bbdd"

router = APIRouter(prefix="/jwt_auth_users",
                   tags=["jwt_auth_users"],
                   responses={404: {"description": "Not found"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "sbauza": {
        "username": "sbauza",
        "full_name": "Santiago Bauza",
        "email": "s.bauza@alumnos.upm.es",
        "disabled": False,
        "password": "$2a$12$FESFdKp5KNpABU70cGQjwOk4UBqz/dmbdGQ95UpmZekm0kSQwAc.y"
    },
    "sbauza2": {
        "username": "sbauza2",
        "full_name": "Santiago Bauza 2",
        "email": "s.bauza2@alumnos.upm.es",
        "disabled": True,
        "password": "$2a$12$kDh0pI9sHw90DShe.hOQ4ON3x7wzCjwwWkYDF2w0lrRm3ieMJHcZ6"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def auth_user(token: str = Depends(oauth2)):
    
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                              detail="Invalid authentication credentials",
                              headers={"WWW-Authenticate": "Bearer"})
    
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
        
    except jwt.PyJWTError:
        raise exception
    
    return search_user(username)

    
async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Inactive user")
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = search_user_db(form.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username")

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")

    access_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user