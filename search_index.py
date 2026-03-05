from fastapi import APIRouter

router = APIRouter()

index_data = []

@router.post("/index-data")

def index_data_store(domain: str, keyword: str):

    entry = {
        "domain": domain,
        "keyword": keyword
    }

    index_data.append(entry)

    return {
        "status": "indexed",
        "entry": entry
    }


@router.get("/search-index")

def search_index():

    return {
        "index": index_data
    }
