from fastapi import APIRouter

router = APIRouter()

@router.get("/link-building")

def link_building(domain: str):

    links = [
        "guest posting sites",
        "blog commenting",
        "forum backlinks",
        "directory submission",
        "web 2.0 blogs"
    ]

    return {
        "domain": domain,
        "link_strategy": links
    }
