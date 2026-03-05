from fastapi import APIRouter
import random

router = APIRouter()

actions = [
    "Create new SEO blog",
    "Build backlinks",
    "Optimize existing content",
    "Target long-tail keywords"
]

@router.get("/ai-decision")

def ai_decision(domain: str):

    decision = random.choice(actions)

    return {
        "domain": domain,
        "next_action": decision
    }
