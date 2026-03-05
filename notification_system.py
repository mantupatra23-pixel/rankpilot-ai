from fastapi import APIRouter

router = APIRouter()

@router.get("/notifications")

def notifications():

    messages = [
        "SEO audit completed",
        "New keyword opportunity found",
        "Backlink strategy ready"
    ]

    return {
        "notifications": messages
    }
