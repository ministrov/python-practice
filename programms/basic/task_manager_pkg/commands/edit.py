""" Модуль для редактирования задачи """

from task_manager_pkg.tasks.tasks import Task, update_task
from task_manager_pkg.helpers.args import parse_edit
from task_manager_pkg.helpers.table import stringify_table


def edit_command(tasks: list[Task], args: list[str]):
    task_id, changes = parse_edit(args)
    task = list(filter(lambda t: t["id"] == task_id, tasks))
    if len(task) == 0:
        print("Задача не найдена")
        return
    update_task(task[0], **changes)
    print(stringify_table(task))
