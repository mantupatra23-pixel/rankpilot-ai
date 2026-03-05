from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/crawl")

def crawl_site(url: str):

    try:

        response = requests.get(url)

        status = response.status_code

    except:

        status = "error"

    return {
        "url": url,
        "status": status,
        "message": "crawler executed"
    }
