from fastapi import APIRouter

router = APIRouter()

tools = [
    "SEO Audit Tool",
    "Backlink Finder",
    "Keyword Analyzer"
]

@router.get("/marketplace")

def marketplace():

    return {
        "available_tools": tools
    }
