""" Модуль для удаления задачи"""

from task_manager_pkg.tasks.tasks import Task
from task_manager_pkg.tasks.tasks import remove_task


def remove_command(tasks: list[Task], args: list[str]):
    if not args:
        print("Использование: remove <id>")
        return

    try:
        task_id = int(args[0])
    except ValueError:
        print("[ERROR]: id должен быть числом")
        return

    if remove_task(tasks, task_id):
        print(f"Задача {task_id} удалена")
    else:
        print(f"Задача {task_id} не найдена")
