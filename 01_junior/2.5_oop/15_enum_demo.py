# -*- coding: utf-8 -*-
"""
Блок 2.5.8: Демо — Enum (перечисления)
════════════════════════════════════════════════════════════════════════
Темы:
  1. Проблема без Enum: "магические" строки/числа без валидации
  2. enum.Enum — именованные константы, сгруппированные в один тип
  3. auto() — автогенерация значений, когда конкретное значение не важно
  4. Доступ к имени/значению, сравнение членов, итерация по классу
  5. IntEnum — когда нужна совместимость с int (сортировка, сравнение)
  6. Практическая польза: Enum в аннотациях типов + match
"""

from enum import Enum, IntEnum, auto


# ════════════════════════════════════════════════════════════════════════
# 1. Проблема без Enum: "магические" строки без валидации
# ════════════════════════════════════════════════════════════════════════


def ship_order_plain(status: str) -> None:
    if status == "pending":
        print("Заказ ожидает обработки")
    elif status == "shipped":
        print("Заказ отправлен")
    else:
        print(f"Неизвестный статус: {status}")


ship_order_plain("shiped")  # опечатка — никто не поймает её до рантайма
# Неизвестный статус: shiped
# Строка — любой текст. Опечатку не видит ни линтер, ни pyright.


# ════════════════════════════════════════════════════════════════════════
# 2. enum.Enum — именованные константы, сгруппированные в один тип
# ════════════════════════════════════════════════════════════════════════


class OrderStatus(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"


print(OrderStatus.PENDING)  # OrderStatus.PENDING
print(OrderStatus.PENDING.name)  # PENDING
print(OrderStatus.PENDING.value)  # pending
# OrderStatus.SHIPED — опечатка здесь упадёт с AttributeError СРАЗУ,
# а pyright --strict подсветит её ещё ДО запуска


# ════════════════════════════════════════════════════════════════════════
# 3. auto() — автогенерация значений, когда конкретное значение не важно
# ════════════════════════════════════════════════════════════════════════


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


print(Direction.UP.value)  # 1
print(Direction.RIGHT.value)  # 4
# auto() присваивает 1, 2, 3... по порядку объявления — используем,
# когда важны только РАЗЛИЧНЫЕ значения, а не конкретные числа


# ════════════════════════════════════════════════════════════════════════
# 4. Доступ к имени/значению, сравнение членов, итерация по классу
# ════════════════════════════════════════════════════════════════════════

status = OrderStatus.SHIPPED

print(status == OrderStatus.SHIPPED)  # True
print(status is OrderStatus.SHIPPED)  # True — члены Enum это синглтоны
print(status == "shipped")  # type: ignore  # намеренно: False — сравнение
# с value НЕ равно сравнению с самим членом Enum. pyright --strict даже
# подсвечивает это КАК ОШИБКУ (reportUnnecessaryComparison) — типы
# OrderStatus и str в принципе не пересекаются

for member in OrderStatus:
    print(member.name, "->", member.value)
# PENDING -> pending
# SHIPPED -> shipped
# DELIVERED -> delivered


# ════════════════════════════════════════════════════════════════════════
# 5. IntEnum — когда нужна совместимость с int (сортировка, сравнение)
# ════════════════════════════════════════════════════════════════════════


class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


print(Priority.HIGH > Priority.LOW)  # True — обычный Enum так не умеет
print(Priority.HIGH == 3)  # True — IntEnum ведёт себя как int
print(sorted([Priority.HIGH, Priority.LOW, Priority.MEDIUM]))
# [<Priority.LOW: 1>, <Priority.MEDIUM: 2>, <Priority.HIGH: 3>]


# ════════════════════════════════════════════════════════════════════════
# 6. Практическая польза: Enum в аннотациях типов + match
# ════════════════════════════════════════════════════════════════════════


def describe_status(status: OrderStatus) -> str:
    match status:
        case OrderStatus.PENDING:
            return "Ожидает обработки"
        case OrderStatus.SHIPPED:
            return "В пути"
        case OrderStatus.DELIVERED:
            return "Доставлен"


print(describe_status(OrderStatus.SHIPPED))  # В пути
# describe_status("shiped") — pyright --strict подсветит несовпадение
# типов ЕЩЁ ДО запуска: функция принимает только OrderStatus, а не str
