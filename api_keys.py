from fastapi import APIRouter
import uuid

router = APIRouter()

api_keys = {}

@router.post("/generate-api-key")
def generate_key(user: str):

    key = str(uuid.uuid4())

    api_keys[user] = key

    return {
        "user": user,
        "api_key": key
    }

@router.get("/api-keys")
def list_keys():

    return api_keys
