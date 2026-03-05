from fastapi import APIRouter
import threading
import time

router = APIRouter()

workers = []

def worker_task(task_name):

    for i in range(3):

        print(f"Running task: {task_name}")

        time.sleep(5)

@router.post("/start-worker")

def start_worker(task: str):

    thread = threading.Thread(target=worker_task, args=(task,))

    thread.start()

    workers.append(task)

    return {
        "status": "worker started",
        "task": task
    }


@router.get("/workers")

def list_workers():

    return {
        "active_tasks": workers
    }
