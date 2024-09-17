from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entitie User


class User(BaseModel):
    id: int
    name: str
    age: int


user_list = [User(id=1, name="Santiago", age=28),
             User(id=2, name="Juan", age=30),
             User(id=3, name="Pedro", age=25)]


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Santiago", "age": 28},
            {"name": "Juan", "age": 30},
            {"name": "Pedro", "age": 25}]


@app.get("/users")
async def users():
    return user_list

# Path


@app.get("/users/{id}")  # /users/1
async def user(id: int):
    return search_user(id)

# Query


@app.get("/userquery/")  # /userquery/?id=1
async def user(id: int):
    return search_user(id)


@app.post("/user/")
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        return {"message": "User already exists"}
    else:
        user_list.append(user)


@app.put("/user/")
async def update_user(user: User):
    if type(search_user(user.id)) == User:
        user_list.remove(search_user(user.id))
        user_list.append(user)
        return {"message": "User updated"}


@app.delete("/user/{id}")
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
