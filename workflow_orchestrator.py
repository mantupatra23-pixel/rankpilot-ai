from fastapi import APIRouter

router = APIRouter()

@router.post("/run-workflow")

def run_workflow(domain: str):

    workflow = [
        "SEO audit",
        "Keyword research",
        "Content generation",
        "Backlink analysis",
        "Rank tracking",
        "SEO report generation"
    ]

    return {
        "domain": domain,
        "workflow_started": True,
        "steps": workflow
    }
