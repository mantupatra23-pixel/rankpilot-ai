from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/dashboard")

def dashboard(domain: str):

    data = {
        "domain": domain,
        "seo_score": random.randint(60, 95),
        "keywords_ranked": random.randint(20, 150),
        "backlinks": random.randint(50, 500),
        "traffic_estimate": random.randint(1000, 20000),
        "ai_suggestion": "Publish 3 new SEO articles and build backlinks"
    }

    return data
