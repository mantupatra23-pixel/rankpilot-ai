from fastapi import APIRouter

router = APIRouter()

models = [
    "seo-content-model",
    "keyword-analysis-model",
    "ranking-prediction-model"
]

@router.get("/models")

def list_models():

    return {
        "ai_models": models
    }


@router.post("/load-model")

def load_model(name: str):

    return {
        "status": "model loaded",
        "model": name
    }
