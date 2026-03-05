from fastapi import APIRouter

router = APIRouter()

@router.get("/seo-score")
def seo_score(domain: str):

    score = 78

    issues = [
        "Missing meta description",
        "Low word count",
        "Few backlinks"
    ]

    return {
        "domain": domain,
        "seo_score": score,
        "issues": issues
    }
