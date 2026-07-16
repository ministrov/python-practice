""" Модуль разбора аргументов"""

from datetime import date, datetime


def parse_list(args: list[str]):
    by = None
    for arg in args:
        if arg.startswith("by="):
            by = arg.split("=", 1)[1]
    return by


def parse_add(args: list[str]):
    if not args:
        raise ValueError(
            "Использование: add <title> [prio=low|med|high] [[due=YYYY-MM-DD] [tags=a,b,c]")
    title = args[0]
    prio, due, tags = "med", None, None

    for arg in args[1:]:
        if arg.startswith("prio="):
            prio = arg.split("=", 1)[1]
        elif arg.startswith("due="):
            due_string = arg.split("=", 1)[1]
            try:
                due = parse_date(due_string)
            except ValueError as e:
                raise ValueError(
                    f"Неверный формат даты: {due_string}. Ожидаем YYYY-MM-DD") from e
        elif arg.startswith("tags="):
            tags_string = arg.split("=", 1)[1]
            tags = tags_string.split(",")
    return title, prio, due, tags


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, "%Y-%m-%d").date()


def parse_edit(args: list[str]) -> tuple[int, dict[str, str | date]]:
    task_id = 0
    if len(args) < 2:
        raise ValueError("Неверно передана команда")
    try:
        task_id = int(args[0])
    except ValueError as e:
        raise ValueError("Неверно передан id задачи") from e

    changes: dict[str, str | date] = {}

    for arg in args[1:]:
        if arg.startswith("title"):
            changes["title"] = arg.split("=", 1)[1]
        if arg.startswith("prio="):
            changes["prio"] = arg.split("=", 1)[1]
        elif arg.startswith("due="):
            due_string = arg.split("=", 1)[1]
            try:
                changes["due"] = parse_date(due_string)
            except ValueError as e:
                raise ValueError(
                    f"Неверный формат даты: {due_string}. Ожидаем YYYY-MM-DD") from e

    return (task_id, changes)
