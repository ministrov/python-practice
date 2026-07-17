""" Модуль для формирования таблицы """

from datetime import date
from task_manager_pkg.tasks.tasks import Task


def format_date(d: date) -> str:
    return date.strftime(d, "%Y-%m-%d")


def stringify_table(tasks: list[Task]) -> str:
    headers = ["ID", "Название", "Статус", "Приоритет", "Теги", "Дата"]
    rows: list[list[str]] = []

    for task in tasks:
        tags = ",".join(sorted(task["tags"])) if task["tags"] else "-"
        rows.append([
            str(task["id"]),
            task["title"],
            task["status"],
            task["priority"],
            tags,
            format_date(task["due"]) if task["due"] else "-"
        ])

    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, col in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(col)))

    def format_row(row: list[str]) -> str:
        return " | ".join(f"{col:<{col_widths[i]}}" for i, col in enumerate(row))

    output: list[str] = []
    output.append(format_row(headers))
    output.append("-+-".join("-" * w for w in col_widths))

    for row in rows:
        output.append(format_row(row))

    return "\n".join(output)
