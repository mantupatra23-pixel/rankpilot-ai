from fastapi import APIRouter
import os
from openai import OpenAI

router = APIRouter()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@router.post("/auto-seo-bot")

def auto_seo(domain: str, niche: str):

    prompt = f"""
    You are an advanced SEO automation AI.

    Domain: {domain}
    Niche: {niche}

    Generate:
    1. 10 ranking keywords
    2. 5 blog titles
    3. 1 full SEO blog article
    4. backlink strategy
    5. growth roadmap
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "domain": domain,
        "automation_result": response.choices[0].message.content
    }
