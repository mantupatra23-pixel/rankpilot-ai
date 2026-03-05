from fastapi import APIRouter

router = APIRouter()

@router.get("/seo-analytics")

def seo_analytics(domain: str):

    data = {
        "domain": domain,
        "traffic": 4200,
        "keywords_ranked": 38,
        "backlinks": 120,
        "seo_score": 81
    }

    return data
