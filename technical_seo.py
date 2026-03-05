from fastapi import APIRouter

router = APIRouter()

@router.get("/technical-seo")
def technical_scan(domain: str):

    report = {
        "domain": domain,
        "page_speed": "Good",
        "mobile_friendly": True,
        "sitemap": "Found",
        "robots_txt": "Found",
        "broken_links": 2
    }

    return report


@router.get("/broken-links")
def broken_links(domain: str):

    links = [
        "https://example.com/old-page",
        "https://example.com/test-link"
    ]

    return {
        "domain": domain,
        "broken_links": links
    }
