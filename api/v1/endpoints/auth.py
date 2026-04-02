from fastapi import APIRouter, Depends, status
from db.mongodb import get_database
from models.user import UserCreate

router = APIRouter()


@router.post("/authenticate", status_code=status.HTTP_200_OK)
async def authenticate_user(user_in: UserCreate, db=Depends(get_database)):
    collection = db["user"]

    # Check if user exists
    existing_user = await collection.find_one({"email": user_in.email})

    if existing_user:
        return {"status": "success", "message": "User already exists"}

    # Create new user if not found
    new_user = await collection.insert_one({"email": user_in.email})
    return {"status": "success", "message": "New user created", "id": str(new_user.inserted_id)}
