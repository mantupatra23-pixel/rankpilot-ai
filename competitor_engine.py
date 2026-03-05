from fastapi import APIRouter

router = APIRouter()


# Competitor Finder
@router.get("/competitors")
def find_competitors(domain: str):

    competitors = [
        "competitor1.com",
        "competitor2.com",
        "competitor3.com"
    ]

    return {
        "domain": domain,
        "competitors": competitors
    }


# Keyword Gap Engine
@router.get("/keyword-gap")
def keyword_gap(domain: str):

    keywords = [
        "seo tools",
        "seo audit tool",
        "keyword research tool",
        "rank tracker"
    ]

    return {
        "domain": domain,
        "competitor_keywords": keywords
    }


# Content Gap Analyzer
@router.get("/content-gap")
def content_gap(domain: str):

    gaps = [
        "SEO tutorial",
        "keyword research guide",
        "technical SEO checklist"
    ]

    return {
        "domain": domain,
        "content_gaps": gaps
    }
