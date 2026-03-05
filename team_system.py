from fastapi import APIRouter

router = APIRouter()

team = []

@router.post("/add-team-member")

def add_member(name: str, role: str):

    member = {
        "name": name,
        "role": role
    }

    team.append(member)

    return {
        "status": "member added",
        "member": member
    }


@router.get("/team")

def list_team():

    return {
        "team": team
    }
