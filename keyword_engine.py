from fastapi import APIRouter

router = APIRouter()

@router.get("/keywords")
def keyword_research(topic: str):

    keywords = [
        topic + " tips",
        topic + " tools",
        topic + " strategy",
        topic + " guide"
    ]

    return {
        "topic": topic,
        "keywords": keywords
    }
