from fastapi import APIRouter

router = APIRouter()

@router.post("/start-ai-agent")

def start_agent(domain: str):

    process = [
        "Running SEO audit",
        "Finding keywords",
        "Generating blog content",
        "Creating backlink strategy",
        "Analyzing SEO performance"
    ]

    return {
        "domain": domain,
        "ai_agent_status": "running",
        "steps": process
    }
