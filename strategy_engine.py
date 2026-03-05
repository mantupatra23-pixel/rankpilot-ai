from fastapi import APIRouter

router = APIRouter()

@router.get("/seo-strategy")

def seo_strategy(domain: str):

    plan = {
        "domain": domain,
        "month_plan": {
            "week1": "SEO audit and keyword research",
            "week2": "Publish 3 blog posts",
            "week3": "Build 10 backlinks",
            "week4": "Promote content on social media"
        }
    }

    return plan
