""" Функция для создания задачи с различными параметрами """

from typing import TypedDict


class Task(TypedDict):
    id: int
    title: str
    priority: str
    tags: list[str]
    status: str


def make_task(object: Task):
    pass
