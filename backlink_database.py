from fastapi import APIRouter

router = APIRouter()

@router.get("/backlink-database")

def backlink_database(domain: str):

    backlinks = [
        "news-site.com",
        "tech-blog.com",
        "seo-directory.com",
        "guestpost-site.com"
    ]

    return {
        "domain": domain,
        "backlink_sources": backlinks
    }
