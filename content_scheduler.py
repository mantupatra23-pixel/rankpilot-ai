from fastapi import APIRouter
import os
from openai import OpenAI

router = APIRouter()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@router.post("/content-scheduler")

def schedule_content(domain: str, niche: str):

    prompt = f"""
    You are an SEO content planner.

    Website: {domain}
    Niche: {niche}

    Create:
    1. 7 daily blog post ideas
    2. 7 social media posts
    3. SEO task schedule for 1 week
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "domain": domain,
        "weekly_plan": response.choices[0].message.content
    }
