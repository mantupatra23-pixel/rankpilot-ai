from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/keyword-difficulty")

def keyword_difficulty(keyword: str):

    difficulty = random.randint(1, 100)

    return {
        "keyword": keyword,
        "difficulty_score": difficulty
    }
