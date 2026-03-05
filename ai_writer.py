from fastapi import APIRouter

router = APIRouter()

def generate_article(keyword: str):

    article = f"""
    Title: Complete Guide to {keyword}

    Introduction:
    This article explains everything about {keyword}.

    Section 1:
    Best strategies for {keyword}

    Section 2:
    Tools and methods related to {keyword}

    Conclusion:
    Follow these steps to improve your SEO using {keyword}.
    """

    return article


@router.get("/ai-content")

def ai_content(keyword: str):

    article = generate_article(keyword)

    return {
        "keyword": keyword,
        "article": article
    }
