from fastapi import FastAPI, HTTPException, Query
from models.task import TaskCreate, TaskUpdate, TaskStatus
from utils.responseOrder import order_task_fields

app = FastAPI()

# Armazenamento em memória das tarefas
tasks = []
last_id = 0 # Último ID gerado

@app.get("/tasks")
async def list_tasks():
    """
    Lista todas as tarefas.
    """
    sorted_tasks = sorted(tasks, key=lambda x: x["id"])
    ordered_tasks = [order_task_fields(task) for task in sorted_tasks]
    return {
        "status": "success",
        "message": "Tasks retrieved successfully.",
        "data": ordered_tasks
    }

@app.get("/tasks/{task_id}")
async def get_task_by_id(task_id: int):
    """
    Recupera uma tarefa pelo ID.
    """
    for task in tasks:
        if task["id"] == task_id:
            ordered_task = order_task_fields(task)
            return {
                "status": "success",
                "message": "Task retrieved successfully.",
                "data": ordered_task
            }
    raise HTTPException(status_code=404, detail="Task not found.")

@app.get("/tasks_search")
async def search_tasks_by_title(title: str = Query(...)):
    """
    Procura tarefas pelo título.
    """
    matching_tasks = [task for task in tasks if title.lower() in task["title"].lower()]
    if matching_tasks:
        ordered_tasks = [order_task_fields(task) for task in matching_tasks]
        return {
            "status": "success",
            "message": "Tasks retrieved successfully.",
            "data": ordered_tasks
        }
    raise HTTPException(status_code=404, detail="No tasks found with the given title.")

@app.post("/tasks", status_code=201)
async def create_task(task: TaskCreate):
    """
    Adiciona uma nova tarefa.
    """
    global last_id
    last_id += 1
    task_data = task.dict()
    task_data["id"] = last_id
    tasks.append(task_data)

    ordered_task_data = order_task_fields(task_data)
    return {
        "status": "success",
        "message": "Task added successfully.",
        "data": ordered_task_data
    }

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: TaskUpdate):
    """
    Atualiza os dados de uma tarefa pelo ID.
    """
    for existing_task in tasks:
        if existing_task["id"] == task_id:
            existing_task.update(task.dict())
            ordered_task = order_task_fields(existing_task)
            return {
                "status": "success",
                "message": "Task updated successfully.",
                "data": ordered_task
            }
    raise HTTPException(status_code=404, detail="Task not found.")

@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int):
    """
    Deleta uma tarefa pelo ID.
    """
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return
    raise HTTPException(status_code=404, detail="Task not found.")