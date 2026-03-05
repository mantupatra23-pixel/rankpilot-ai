from fastapi import APIRouter

router = APIRouter()

database = []

@router.post("/store-data")

def store_data(domain: str, keyword: str):

    entry = {
        "domain": domain,
        "keyword": keyword
    }

    database.append(entry)

    return {
        "status": "stored",
        "data": entry
    }


@router.get("/data")

def get_data():

    return database
