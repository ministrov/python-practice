# Python Backend Developer Journey

> Практический курс: от нуля до Python backend разработчика
> Старт: 2026-06-06 | Уровень: Junior | Блок 2.7 — ошибки и исключения — ЗАВЕРШЁН (все 5 тем, 2026-08-19); далее Блок 2.8 (БД и SQL)

## Цель проекта

Структурированный путь обучения Python с фокусом на backend разработку.
Стек-ориентир: Python 3.12+, FastAPI, PostgreSQL, SQLAlchemy, Docker, Kubernetes.
Длительность: 18-24 месяца при 10-15 часах в неделю.

---

## Текущий прогресс

| Блок | Тема | Статус |
|------|------|--------|
| 2.1 | Фундамент языка | ЗАВЕРШЕН |
| 2.2 | Структуры данных | ЗАВЕРШЕН (финальная оценка пройдена 2026-07-24, 100%) |
| 2.3 | Функции | ЗАВЕРШЕН (финальная оценка пройдена 2026-07-24, 100%) |
| 2.4 | Модули, файлы и дата/время | ЗАВЕРШЕН (все 3 темы, 2026-07-24) |
| 2.5 | ООП и модель данных | ЗАВЕРШЕН (финальная оценка пройдена 2026-08-14, 100%) |
| 2.6 | Типизация и качество кода | ЗАВЕРШЕН (все 5 тем, 2026-08-18) |
| 2.7 | Ошибки и исключения | ЗАВЕРШЕН (тема 1: 8/8, тема 2: 7/7, темы 3-5 ознакомительно, 2026-08-19) |
| 2.8–2.10 | БД, FastAPI, Git | Запланировано |

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
├── 2.2_data_structures/        # ЗАВЕРШЕН (финальная оценка 100%, 2026-07-24)
│   ├── 01_list_demo.py + 02_list_task.py
│   ├── 03_tuple_demo.py + 04_tuple_task.py
│   ├── 05_dict_demo.py + 06_dict_task.py
│   ├── 07_set_demo.py + 08_set_task.py
│   ├── 09_list_comprehensions_demo.py + 10_list_comprehensions_task.py
│   └── 11_choosing_structures_demo.py + 12_choosing_structures_task.py
│
├── 2.3_functions/              # ЗАВЕРШЕН (финальная оценка 100%, 2026-07-24)
│   ├── 01_functions_basics_demo.py + 02_functions_basics_task.py
│   ├── 03_args_kwargs_demo.py + 04_args_kwargs_task.py
│   ├── 05_legb_demo.py + 06_legb_task.py
│   ├── 07_functions_as_objects_demo.py + 08_functions_as_objects_task.py
│   └── 09_higher_order_pitfalls_task.py    # закрепление темы 4, мини-тест 5/5
│
├── 2.4_modules_files_datetime/ # ЗАВЕРШЕН (все 3 темы, 2026-07-24)
│   ├── 01_modules_demo.py + 02_modules_task.py (8/8)
│   ├── geometry.py, shapes_pkg/           # фикстуры для demo (не редактировать)
│   ├── string_utils.py, text_report.py    # решения заданий 1-2,4-5,8
│   ├── text_pkg/                          # решение задания 6 (свой пакет)
│   ├── 03_files_advanced_demo.py + 04_files_advanced_task.py (8/8)
│   └── 05_datetime_demo.py + 06_datetime_task.py (8/8)
├── 2.5_oop/                    # ЗАВЕРШЕН (все 9 тем, 2026-08-13)
│   ├── 01_classes_demo.py + 02_classes_task.py (8/8)
│   ├── 03_methods_demo.py + 04_methods_task.py (8/8)
│   ├── 05_inheritance_demo.py + 06_inheritance_task.py (8/8)
│   ├── 07_composition_demo.py + 08_composition_task.py (8/8)
│   ├── 09_dataclasses_demo.py + 10_dataclasses_task.py (8/8)
│   ├── 11_dunder_methods_demo.py + 12_dunder_methods_task.py (8/8)
│   ├── 13_abstraction_demo.py + 14_abstraction_task.py (8/8)
│   ├── 15_enum_demo.py + 16_enum_task.py (7/7)
│   └── 17_four_pillars_demo.py + 18_four_pillars_task.py (5/5)
├── 2.6_typing/                 # ЗАВЕРШЕН (все 5 тем, 2026-08-18)
│   ├── 01_type_annotations_demo.py + 02_type_annotations_task.py (8/8)
│   ├── 03_typing_module_demo.py + 04_typing_module_task.py (8/8)
│   ├── 05_type_checking_setup_demo.py       # ознакомительно, mypy/pyright
│   ├── 07_pep8_formatting_linting_demo.py   # ознакомительно, ruff/black
│   └── 08_venv_pip_requirements_demo.py     # ознакомительно, venv/pip
├── 2.7_exceptions/             # ЗАВЕРШЕН (все 5 тем, 2026-08-19)
│   ├── 01_exceptions_basics_demo.py + 02_exceptions_basics_task.py (8/8)
│   ├── 03_raise_from_demo.py + 04_raise_from_task.py (7/7, 2026-08-19)
│   ├── 05_context_managers_demo.py          # ознакомительно
│   ├── 06_stdlib_demo.py                    # ознакомительно
│   └── 07_logging_demo.py                   # ознакомительно
├── 2.8_databases/              # Запланировано
├── 2.9_fastapi/                # Запланировано
│
02_middle/    # Запланировано: async, БД, FastAPI, тестирование
03_senior/    # Запланировано: архитектура, распределённые системы, DevOps
```

Папка `assessments/` находится в корне репозитория (не в `01_junior/`):

```
assessments/
├── ASSESSMENT_Block_2_1.md      # Пройдена
├── REASSESSMENT_Block_2_1.md    # Пройдена
├── ASSESSMENT_Block_2_2.md      # Пройдена (100%, 2026-07-24)
├── ASSESSMENT_Block_2_3.md      # Пройдена (100%, 2026-07-24)
└── ASSESSMENT_Block_2_5.md      # Пройдена (100%, 2026-08-14)
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
| Junior  | 2.1-2.7 завершены (2.5 ООП: 9 тем + финальная оценка 100%; 2.6 типизация: все 5 тем; 2.7 ошибки/исключения: все 5 тем); далее 2.8 (БД и SQL) | В работе |
| Middle  | — | Запланировано |
| Senior  | — | Запланировано |

---

**Последнее обновление:** 2026-08-19 (блок 2.7 полностью завершён — тема 1 try/except 8/8, тема 2 `raise from`/`ExceptionGroup` 7/7, темы 3-5 контекстные менеджеры/stdlib/logging ознакомительно; далее блок 2.8, базы данных и SQL)
**Python:** 3.12+
