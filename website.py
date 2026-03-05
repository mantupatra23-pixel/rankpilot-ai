from fastapi import APIRouter

router = APIRouter()

websites = []

@router.post("/add-website")
def add_website(domain: str):
    websites.append(domain)
    return {"message": "website added", "domain": domain}
