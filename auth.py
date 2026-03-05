from fastapi import APIRouter

router = APIRouter()

users = []

@router.post("/register")
def register(email: str, password: str):
    users.append({"email": email, "password": password})
    return {"message": "user registered"}

@router.post("/login")
def login(email: str, password: str):
    for user in users:
        if user["email"] == email and user["password"] == password:
            return {"message": "login success"}
    return {"message": "invalid credentials"}
