from fastapi import APIRouter

router = APIRouter()

@router.get("/plans")
def plans():

    plans = [
        {"name": "Starter", "price": "₹999/month"},
        {"name": "Pro", "price": "₹2999/month"},
        {"name": "Agency", "price": "₹9999/month"}
    ]

    return {"plans": plans}


@router.post("/subscribe")
def subscribe(plan: str):

    return {
        "status": "subscription activated",
        "plan": plan
    }
