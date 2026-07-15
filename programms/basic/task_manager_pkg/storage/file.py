""" Модуль хранилище данных """

import json
from typing import Any
from task_manager_pkg.helpers.table import format_date
from task_manager_pkg.tasks.tasks import Task
from task_manager_pkg.helpers.args import parse_date


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


def load_tasks(path: str) -> tuple[list[Task], int]:
    raw: dict[str, Any] = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except FileNotFoundError:
        return [], 1
    except json.JSONDecodeError as e:
        print(f"[WARN] Поврежденный JSON ({path}): {e}")
    tasks: list[Task] = []
    max_id = 0

    for item in raw.get("tasks", []):
        try:
            task: Task = {
                "id": int(item["id"]),
                "title": item["title"],
                "priority": item["priority"],
                "tags": list(item.get("tags") or []),
                "status": item["status"],
                "due": parse_date(item["due"]) if item["due"] else None
            }
            tasks.append(task)
            max_id = max(max_id, int(item["id"]))
        except Exception as e:
            print(f"[WARN] Пропущена задача {e}")
    return tasks, max_id + 1
