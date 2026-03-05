from queue import Queue

task_queue = Queue()

def add_task(task):
    task_queue.put(task)

def process_tasks():

    while not task_queue.empty():
        task = task_queue.get()
        print("Processing:", task)
