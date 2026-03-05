from fastapi import APIRouter
from utils import generate_seo_score

router = APIRouter()

@router.get("/seo-audit")
def seo_audit(domain: str):

    score = generate_seo_score()

    return {
        "domain": domain,
        "seo_score": score,
        "issues": [
            "Missing meta description",
            "Low content length",
            "Few backlinks"
        ]
    }
