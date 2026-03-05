from fastapi import APIRouter

router = APIRouter()

@router.get("/rank-check")

def rank_check(domain: str, keyword: str):

    rank = 12

    return {
        "domain": domain,
        "keyword": keyword,
        "google_rank": rank
    }
