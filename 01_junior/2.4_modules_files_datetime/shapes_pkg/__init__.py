# -*- coding: utf-8 -*-
"""
shapes_pkg — вспомогательный пакет для demo/task по теме "Модули"
(Блок 2.4.1). Не редактировать. Показывает, что __init__.py выполняется
при первом импорте пакета и может поднимать имена из вложенных модулей
наверх, чтобы снаружи не писать shapes_pkg.circle.describe_circle.
"""

print(f"[shapes_pkg] пакет инициализируется (__name__ = {__name__!r})")

from .circle import describe_circle

__all__ = ["describe_circle"]
