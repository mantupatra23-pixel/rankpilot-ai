from fastapi import APIRouter

router = APIRouter()

@router.get("/websites")

async def get_websites():

    return {"websites": []}
