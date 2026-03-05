from fastapi import APIRouter

router = APIRouter()

usage = {}

@router.post("/track-usage")
def track_usage(user: str):

    if user not in usage:
        usage[user] = 0

    usage[user] += 1

    return {
        "user": user,
        "requests": usage[user]
    }

@router.get("/usage")
def get_usage():

    return usage
