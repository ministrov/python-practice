# Python Backend Developer Journey

> Практический курс: от нуля до Python backend разработчика
> Старт: 2026-06-06 | Уровень: Junior | Текущий блок: 2.3 — Функции (темы 1-4 завершены + закрепление темы 4 — 2026-07-09)

## Цель проекта

Структурированный путь обучения Python с фокусом на backend разработку.
Стек-ориентир: Python 3.12+, FastAPI, PostgreSQL, SQLAlchemy, Docker, Kubernetes.
Длительность: 18-24 месяца при 10-15 часах в неделю.

---

## Текущий прогресс

| Блок | Тема | Статус |
|------|------|--------|
| 2.1 | Фундамент языка | ЗАВЕРШЕН |
| 2.2 | Структуры данных | Задания завершены, оценка 2026-06-27 |
| 2.3 | Функции | В процессе |
| 2.4–2.9 | ООП, типизация, БД, FastAPI, Git | Запланировано |

---

## Структура репозитория

```
01_junior/
├── 2.1_fundamentals/           # ЗАВЕРШЕН
│   ├── 01_types_demo.py + 02_types_task.py
│   ├── 03_variables_demo.py + 03b_variables_task.py
│   ├── 03c_references_and_objects_demo.py + 03c_references_and_objects_task.py
│   ├── 04_is_vs_equals_demo.py + 05_is_vs_equals_task.py
│   ├── 06_conditionals_demo.py + 07_conditionals_task.py
│   ├── 08_practice_30_tasks.py
│   ├── 09_match_case_demo.py + 10_match_case_tasks.py
│   ├── 11_loops_demo.py + 12_loops_tasks.py
│   ├── 13_f_strings_and_string_methods_demo.py + 14_..._tasks.py
│   └── 15_io_and_files_demo.py + 16_io_and_files_tasks.py
│
├── 2.2_data_structures/        # Задания завершены
│   ├── 01_list_demo.py + 02_list_task.py
│   ├── 03_tuple_demo.py + 04_tuple_task.py
│   ├── 05_dict_demo.py + 06_dict_task.py
│   ├── 07_set_demo.py + 08_set_task.py
│   ├── 09_list_comprehensions_demo.py + 10_list_comprehensions_task.py
│   └── 11_choosing_structures_demo.py + 12_choosing_structures_task.py
│
├── 2.3_functions/              # В процессе (темы 1-4 завершены)
│   ├── 01_functions_basics_demo.py + 02_functions_basics_task.py
│   ├── 03_args_kwargs_demo.py + 04_args_kwargs_task.py
│   ├── 05_legb_demo.py + 06_legb_task.py
│   ├── 07_functions_as_objects_demo.py + 08_functions_as_objects_task.py
│   ├── 09_higher_order_pitfalls_task.py    # закрепление темы 4, мини-тест 5/5
│   └── (далее: decorators)
│
├── 2.4_oop/                    # Запланировано
├── 2.5_typing/                 # Запланировано
├── 2.6_exceptions/             # Запланировано
├── 2.7_databases/              # Запланировано
├── 2.8_fastapi/                # Запланировано
│
└── assessments/
    ├── ASSESSMENT_Block_2_1.md     # Пройдена
    ├── REASSESSMENT_Block_2_1.md   # Пройдена
    └── ASSESSMENT_Block_2_2.md     # Запланирована на 2026-06-27

02_middle/    # Запланировано: ООП, async, БД, FastAPI, тестирование
03_senior/    # Запланировано: архитектура, распределённые системы, DevOps
```

---

## Как работать с материалом

Каждая тема состоит из двух файлов:

```bash
# 1. Читай теорию и запускай демо
python 01_junior/2.3_functions/01_functions_basics_demo.py

# 2. Решай задания
python 01_junior/2.3_functions/02_functions_basics_task.py
```

Порядок изучения — по номерам файлов внутри каждого блока.

---

## Требования

- Python 3.12+
- Git
- VS Code с расширением Pylance (typeCheckingMode: strict)

---

## Статистика

| Уровень | Блоков | Статус |
|---------|--------|--------|
| Junior  | 2.1 завершён, 2.2 почти, 2.3 в процессе | В работе |
| Middle  | — | Запланировано |
| Senior  | — | Запланировано |

---

**Последнее обновление:** 2026-07-09 (сеанс 11: закрепление темы 4, мини-тест 5/5)
**Python:** 3.12+
