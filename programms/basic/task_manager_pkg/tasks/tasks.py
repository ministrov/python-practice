""" Модуль, который создает функцию, которая создает задачи с различными параметрами """

from typing import TypedDict, Optional
from datetime import date

PRIORITIES = {"low", "med", "high"}


class Task(TypedDict):
    id: int
    title: str
    priority: str
    tags: list[str]
    status: str
    due: Optional[date]


def create_task(id_: int, title: str, due: Optional[date] = None, priority: str = "med", tags: list[str] | None = None) -> Task:
    if tags is None:
        tags = []

    if priority not in PRIORITIES:
        raise ValueError("Неверный приоритет. Можно только low | med | high")

    task: Task = {
        "id": id_,
        "title": title.strip(),
        "due": due,
        "priority": priority,
        "tags": tags,
        "status": "new",
    }
    return task


def remove_task(tasks: list[Task], task_id: int) -> bool:
    before_len = len(tasks)
    tasks[:] = list(filter(lambda t: t["id"] != task_id, tasks))
    return len(tasks) < before_len
