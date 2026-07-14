""" Модуль разбора аргументов"""

from datetime import date, datetime


def parse_add(args: list[str]):
    if not args:
        raise ValueError(
            "Использование: add <title> [prio=low|med|high] [[due=YYYY-MM-DD] [tags=a,b,c]")
    # title = args[0]
    # prio, due, tags = "med", None, None

    for arg in args[1:]:
        if arg.startswith("prio="):
            pass
            # prio = arg.split("=", 1)[1]
        elif arg.startswith("due="):
            pass
            # due_string = args.split("=", 1)[1]
            # due = parse_date(due_string)
        elif arg.startswith("tags="):
            pass


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, "%Y-%m-%d").date()
