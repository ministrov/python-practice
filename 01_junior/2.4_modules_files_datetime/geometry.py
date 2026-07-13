# -*- coding: utf-8 -*-
"""
geometry.py — вспомогательный модуль для demo/task по теме "Модули"
(Блок 2.4.1). Не редактировать: используется как импортируемый модуль
в 01_modules_demo.py и 02_modules_task.py.
"""

print(f"[geometry] модуль загружается (__name__ = {__name__!r})")

PI = 3.14159


def circle_area(radius: float) -> float:
    """Возвращает площадь круга по радиусу."""
    return PI * radius ** 2


def circle_circumference(radius: float) -> float:
    """Возвращает длину окружности по радиусу."""
    return 2 * PI * radius


def rectangle_area(width: float, height: float) -> float:
    """Возвращает площадь прямоугольника."""
    return width * height


if __name__ == "__main__":
    print("geometry.py запущен напрямую (не импортирован)")
    print(f"Площадь круга радиусом 5: {circle_area(5)}")
