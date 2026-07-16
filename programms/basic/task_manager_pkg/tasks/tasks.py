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


def update_task(task: Task, **changes: str | date | None):
    if "title" in changes:
        title = str(changes["title"]).strip()

        if not title:
            raise ValueError("Заголовок не может быть пустым")
        task["title"] = title

    if "priority" in changes:
        prio = str(changes["priority"]).strip().lower()

        if prio not in PRIORITIES:
            raise ValueError("Неверный приоритет. Только low | med | high")
        task["priority"] = prio

    if "due" in changes:
        due = changes["due"]

        if due is not None and not isinstance(due, date):
            raise TypeError("Поле due должно быть date или None")
        task["due"] = due


def find_task(tasks: list[Task], id_: int) -> Optional[Task]:
    return next((t for t in tasks if t["id"] == id_), None)
