""" Модуль для добавления команды """
from task_manager_pkg.tasks.tasks import create_task, Task
from task_manager_pkg.helpers.args import parse_add
from task_manager_pkg.helpers.table import stringify_table


def add_command(tasks: list[Task], args: list[str], next_id: int) -> int:
    try:
        title, prio, due, tags = parse_add(args)
        task = create_task(next_id, title, due, prio, tags)
        tasks.append(task)
        print("Добавлена задача")
        print(stringify_table([task]))
        return next_id + 1
    except ValueError as e:
        print(f"Ошибка {e}")
        return next_id
