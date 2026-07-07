""" 
    В этой лекции мы рассматриваем упражнение для работы с функцией sorted и предыдущими концепциями, изученными в модуле. Вот шаги, которые нужно выполнить:

    Фильтрация активных сотрудников:

    Используем filter с лямбда-функцией, чтобы оставить только тех сотрудников, у которых поле active равно True.
    Преобразование структуры данных:

    Применяем map с лямбда-функцией, чтобы оставить только name и salary для каждого активного сотрудника, убрав департамент и статус активности.
    Сортировка сотрудников:

    Используем функцию sorted для сортировки сотрудников по убыванию salary. Для этого указываем лямбда-функцию с отрицательным salary, чтобы выполнять сортировку от большего к меньшему.
    Подсчет суммы зарплат:

    Применяем функцию reduce для суммирования всех зарплат. Аккумулятор начинает с нуля, к которому добавляется salary каждого сотрудника.
    Вывод результатов:

    Выводим список сотрудников, отсортированных по зарплате, и общую сумму зарплат.
    Этот последовательный подход помогает лучше понимать каждый этап обработки данных. Выполнив упражнение, мы выделили активных сотрудников, убрали лишние поля, отсортировали по зарплате и вычислили общую сумму выплат. Это удобнее делать поэтапно для лучшей читабельности кода.
"""

from functools import reduce
from typing import TypedDict


class Employee(TypedDict):
    name: str
    department: str
    salary: int
    active: bool


employees: list[Employee] = [
    {"name": "Иван Петров", "department": "IT", "salary": 85000, "active": True},
    {"name": "Мария Сидорова", "department": "HR", "salary": 65000, "active": True},
    {"name": "Алексей Смирнов", "department": "Sales",
        "salary": 70000, "active": False},
    {"name": "Ольга Кузнецова", "department": "Marketing",
        "salary": 72000, "active": True},
    {"name": "Дмитрий Волков", "department": "IT", "salary": 90000, "active": True},
    {"name": "Екатерина Новикова", "department": "Finance",
        "salary": 78000, "active": False},
    {"name": "Сергей Морозов", "department": "Sales",
        "salary": 68000, "active": True},
    {"name": "Анна Лебедева", "department": "HR", "salary": 63000, "active": True},
]

active_employees = list(filter(lambda item: item["active"], employees))
sorted_employees = sorted(
    active_employees, key=lambda item: item["salary"])
sum_of_all_salary = reduce(
    lambda acc, item: acc + item["salary"], sorted_employees, 0)

print(sum_of_all_salary)
