# Python Backend Developer Journey

> Практический курс: от нуля до Python backend разработчика
> Старт: 2026-06-06 | Уровень: Junior | Текущий блок: 2.5 — ООП и модель данных, темы 1-2 завершены (2026-07-21); 2026-07-24 — отработка отложенных долгов

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
| 2.5 | ООП и модель данных | 🔄 В процессе, темы 1-2 завершены (2026-07-21) |
| 2.6 | Типизация и качество кода | Запланировано |
| 2.7 | Ошибки и исключения | Тема 1 завершена 8/8; темы 2–5 — долг (2026-07-24) |
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
├── 2.5_oop/                    # В процессе, темы 1-2 завершены (2026-07-21)
├── 2.6_typing/                 # Запланировано
├── 2.7_exceptions/             # Тема 1 завершена (8/8), темы 2-5 — долг (2026-07-24)
│   ├── 01_exceptions_basics_demo.py + 02_exceptions_basics_task.py (8/8)
│   └── (далее: raise from, контекстные менеджеры, stdlib, logging — долг)
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
└── ASSESSMENT_Block_2_3.md      # Пройдена (100%, 2026-07-24)
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
| Junior  | 2.1, 2.2, 2.3, 2.4 завершены; 2.5 (ООП) в процессе; долг по 2.7 в отработке (2026-07-24) | В работе |
| Middle  | — | Запланировано |
| Senior  | — | Запланировано |

---

**Последнее обновление:** 2026-07-24 (сеанс 20: блок 2.4 полностью завершён — тема 2 "файлы продвинуто" закрыта 8/8; остаётся последний долг — блок 2.7, темы 2-5)
**Python:** 3.12+
