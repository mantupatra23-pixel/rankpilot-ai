from fastapi import APIRouter
import os
from openai import OpenAI

router = APIRouter()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@router.post("/seo-autopilot")

def seo_autopilot(domain: str, niche: str):

    prompt = f"""
    You are an SEO expert.

    Domain: {domain}
    Niche: {niche}

    Generate:
    1. 10 SEO keywords
    2. 5 blog post ideas
    3. 3 backlink strategies
    4. SEO improvement plan
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "domain": domain,
        "seo_plan": response.choices[0].message.content
    }
