""" Модуль разбора аргументов"""

from datetime import date, datetime


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
