from fastapi import APIRouter

router = APIRouter()

@router.get("/generate-blog")
def generate_blog(keyword: str):

    blog = f"""
    Title: {keyword}

    Introduction:
    This article explains {keyword}.

    Section 1:
    Important strategies about {keyword}

    Conclusion:
    Follow these tips to improve SEO.
    """

    return {"blog": blog}
