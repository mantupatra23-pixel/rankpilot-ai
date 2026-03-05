from fastapi import APIRouter

router = APIRouter()

graph = []

@router.post("/add-node")

def add_node(domain: str, keyword: str):

    node = {
        "domain": domain,
        "keyword": keyword
    }

    graph.append(node)

    return {
        "status": "node added",
        "node": node
    }


@router.get("/graph")

def get_graph():

    return {
        "knowledge_graph": graph
    }
