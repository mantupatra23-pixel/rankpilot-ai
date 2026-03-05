from fastapi import APIRouter

router = APIRouter()

projects = []

@router.post("/create-project")

def create_project(name: str, domain: str):

    project = {
        "name": name,
        "domain": domain
    }

    projects.append(project)

    return {
        "status": "project created",
        "project": project
    }


@router.get("/projects")

def list_projects():

    return {
        "projects": projects
    }
