from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: {"description": "Not found"}})

# Entitie User


class User(BaseModel):
    id: int
    name: str
    age: int


user_list = [User(id=1, name="Santiago", age=28),
             User(id=2, name="Juan", age=30),
             User(id=3, name="Pedro", age=25)]


@router.get("/usersjson")
async def usersjson():
    return [{"name": "Santiago", "age": 28},
            {"name": "Juan", "age": 30},
            {"name": "Pedro", "age": 25}]


@router.get("/")
async def users():
    return user_list

# Path


@router.get("/{id}")  # /users/1
async def user(id: int):
    return search_user(id)

# Query


@router.get("/userquery/")  # /userquery/?id=1
async def user(id: int):
    return search_user(id)


@router.post("/user/", response_model= User, status_code=201)
async def create_user(user: User):
    if type(search_user(user.id)) == User:
       raise HTTPException(status_code=204, detail="User already exists")
    else:
        user_list.append(user)
    return user



@router.put("/user/")
async def update_user(user: User):
    if type(search_user(user.id)) == User:
        user_list.remove(search_user(user.id))
        user_list.append(user)
        return {"message": "User updated"}


@router.delete("/user/{id}")
async def delete_user(id: int):
    if type(search_user(id)) == User:
        user_list.remove(search_user(id))
        return {"message": "User deleted"}
    else:
        return {"message": "User not found"}


def search_user(id: int):
    try:
        users = filter(lambda user: user.id == id, user_list)
        return list(users)[0]
    except:
        return {"message": "User not found"}
