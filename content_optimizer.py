from fastapi import APIRouter

router = APIRouter()

@router.post("/optimize-content")

def optimize_content(keyword: str, content: str):

    optimized = f"""
    SEO Optimized Content

    Keyword: {keyword}

    Improved Content:
    {content}

    Suggestions:
    - Add keyword in title
    - Use H1 and H2 headings
    - Increase word count
    """

    return {
        "keyword": keyword,
        "optimized_content": optimized
    }
