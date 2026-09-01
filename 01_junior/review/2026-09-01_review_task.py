"""
Повторение (spaced review) — 2026-09-01

Интегративная мини-задача: "Трекер тикетов поддержки".
Сочетает темы блоков 2.2 (списки/comprehension), 2.3 (функции,
дефолтные аргументы), 2.4 (datetime), 2.5 (классы/dataclass),
2.6 (typing), 2.7 (исключения).

Решение пишется прямо в этот файл, шаг за шагом. Коммит — один,
после того как весь файл запускается без ошибок и печатает
ожидаемые результаты.
"""

from dataclasses import dataclass
from datetime import datetime

ALLOWED_PRIORITIES = ("low", "medium", "high")


# Шаг 1.
# Определи dataclass с именем Ticket с полями:
#   id: int
#   title: str
#   priority: str
#   created_at: datetime
#   resolved: bool = False
# YOUR CODE HERE:

@dataclass
class Ticket:
    id: int
    title: str
    priority: str
    created_at: datetime
    resolved: bool = False


# Шаг 2.
# Напиши функцию create_ticket(id: int, title: str, priority: str) -> Ticket
# Она должна:
#   - проверить, что priority входит в ALLOWED_PRIORITIES,
#     иначе raise ValueError с понятным сообщением
#   - создать и вернуть Ticket с created_at = datetime.now()
# YOUR CODE HERE:

def create_ticket(id: int, title: str, priority: str) -> Ticket:
    if priority not in ALLOWED_PRIORITIES:
        raise ValueError("Такого приоритета не существует")
    else:
        ticket = Ticket(id, title, priority, created_at=datetime.now())
        return ticket

# Шаг 3.
# Напиши функцию safe_create_ticket(id: int, title: str, priority: str) -> Ticket | None
# Она должна вызвать create_ticket внутри try/except ValueError:
#   - при успехе вернуть созданный Ticket
#   - при ValueError напечатать сообщение об ошибке и вернуть None
# YOUR CODE HERE:


# Шаг 4.
# Создай список tickets: list[Ticket], добавив в него результаты
# минимум 6 вызовов safe_create_ticket (учитывая, что safe_create_ticket
# может вернуть None) — среди них должен быть минимум один вызов
# с заведомо неверным priority (например "urgent"), чтобы проверить
# обработку ошибки. None в список не добавлять — фильтруй их.
# YOUR CODE HERE:


# Шаг 5.
# С помощью list comprehension построй high_priority_open: list[Ticket] —
# тикеты из tickets, у которых priority == "high" и resolved is False.
# YOUR CODE HERE:


# Шаг 6.
# Напиши функцию average_age_hours(tickets: list[Ticket]) -> float,
# которая считает среднее время жизни тикетов в часах:
# (datetime.now() - created_at) для каждого тикета, в среднем.
# Если список пустой — вернуть 0.0 (без деления на ноль).
# YOUR CODE HERE:


# Шаг 7.
# Напечатай:
#   - сколько всего тикетов создано успешно
#   - список high_priority_open (title каждого тикета)
#   - среднее время жизни тикетов в часах, округлённое до 4 знаков
# YOUR CODE HERE:
