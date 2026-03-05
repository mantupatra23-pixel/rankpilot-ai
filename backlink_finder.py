from fastapi import APIRouter

router = APIRouter()

@router.get("/backlinks")
def find_backlinks(domain: str):

    backlinks = [
        "directory submission",
        "guest blog",
        "forum profile",
        "web 2.0 blog"
    ]

    return {
        "domain": domain,
        "backlink_sources": backlinks
    }
