from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/usersdb",
                   tags=["usersdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})




@router.get("/", response_model=list[User])  
async def users():
    return users_schema(db_client.users.find())
     


@router.get("/{id}")  
async def user(id: str):
    return search_user("_id", ObjectId(id))



@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    if type(search_user("email", user.email)) == User:
       raise HTTPException(
           status_code=status.HTTP_204_NO_CONTENT, detail="User already exists")

    user_dict = dict(user)

    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return User(**new_user)


@router.put("/",response_model=User)
async def update_user(user: User):
    user_dict = dict(user)
    del user_dict["id"]
    try :
        update_user = db_client.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, dict(user_dict))
    except:
        return {"message": "User not updated"}

    return search_user("_id", ObjectId(user.id))


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        return {"message": "User not found"}


def search_user(field: str, key):
    try:
        user = user_schema(db_client.users.find_one({field: key}))
        return User(**user)
    except:
        return {"message": "User not found"}
