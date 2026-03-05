from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/metrics")

def metrics():

    return {
        "active_users": random.randint(5, 100),
        "running_tasks": random.randint(1, 20),
        "seo_jobs_today": random.randint(10, 200)
    }
