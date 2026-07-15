""" Модуль хранилище данных """

import json
from task_manager_pkg.helpers.table import format_date
from task_manager_pkg.tasks.tasks import Task


def save_task(path: str, tasks: list[Task]):
    data = {
        "tasks": [
            {
                "id": t["id"],
                "title": t["title"],
                "priority": t["priority"],
                "status": t["status"],
                "tags": t["tags"],
                "due": format_date(t["due"]) if t["due"] else None
            }
            for t in tasks
        ],
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
