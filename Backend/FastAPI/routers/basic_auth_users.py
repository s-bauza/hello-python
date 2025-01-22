from fastapi import Depends, status, APIRouter, HTTPException
from pydantic import BaseModel
# OAuth2PasswordBearer is an object that will be used to handle the token
# OAuth2PasswordRequestForm is a class that will be used to handle the form data
# In this case, the form data will be used to get the username and validate the password
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/basic_auth_users",
                   tags=["basic_auth_users"],
                   responses={404: {"description": "Not found"}})

# OAuth2 is a standard for token-based authentication and authorization to handle in the backend.
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

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
        "password": "1234"
    },
    "sbauza2": {
        "username": "sbauza2",
        "full_name": "Santiago Bauza 2",
        "email": "s.bauza2@alumnos.upm.es",
        "disabled": True,
        "password": "12345"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid authentication credentials",
                            headers={"WWW-Authenticate": "Bearer"})
        
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Inactive user")
    return user
    

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = search_user_db(form.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username")
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
    
    return {"access_token": user.username, "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user