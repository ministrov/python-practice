""" Модуль для добавления команды """
from task_manager_pkg.tasks.tasks import create_task, Task
from task_manager_pkg.helpers.args import parse_add


def add_command(tasks: list[Task], args: list[str], next_id: int) -> int:
    try:
        title, prio, due, tags = parse_add(args)
        print(create_task(1, title, due, prio, tags))
    except ValueError as e:
        raise ValueError(f"sdfsfsdfsdf {e}")
    return 0 if "dfdf" else 1
