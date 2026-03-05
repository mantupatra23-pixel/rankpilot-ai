from fastapi import APIRouter

router = APIRouter()

plugins = []

@router.post("/install-plugin")

def install_plugin(name: str):

    plugin = {"plugin": name}

    plugins.append(plugin)

    return {
        "status": "plugin installed",
        "plugin": plugin
    }


@router.get("/plugins")

def list_plugins():

    return {
        "installed_plugins": plugins
    }
