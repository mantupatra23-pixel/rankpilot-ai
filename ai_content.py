from fastapi import APIRouter

router = APIRouter()

@router.get("/generate-content")
def generate_content(keyword: str):
    article = f"SEO article about {keyword}"
    return {
        "keyword": keyword,
        "content": article
    }
