from fastapi import APIRouter
import os
from openai import OpenAI

router = APIRouter()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@router.post("/traffic-strategy")
def traffic_strategy(domain: str, niche: str):

    prompt = f"""
    You are a digital marketing expert.

    Website: {domain}
    Niche: {niche}

    Create a traffic growth plan including:
    1. Reddit content ideas
    2. Quora question answers
    3. Medium blog ideas
    4. Social media content ideas
    5. Weekly traffic strategy
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "domain": domain,
        "traffic_plan": response.choices[0].message.content
    }
