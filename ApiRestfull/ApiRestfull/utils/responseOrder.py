def order_task_fields(task):
    return {
        "id": task["id"],
        "title": task["title"],
        "description": task["description"],
        "status": task["status"]
    }
