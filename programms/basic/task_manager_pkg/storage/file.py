""" Модуль хранилище данных """

import json
from task_manager_pkg.tasks.tasks import Task


def save_task(path: str, tasks: list[Task]):
    data = {
        "tasks": tasks,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
