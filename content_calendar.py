from fastapi import APIRouter

router = APIRouter()

@router.get("/content-calendar")

def content_calendar(topic: str):

    calendar = [
        f"{topic} beginner guide",
        f"{topic} tools",
        f"{topic} strategies",
        f"{topic} mistakes",
        f"{topic} checklist"
    ]

    return {
        "topic": topic,
        "content_plan": calendar
    }
