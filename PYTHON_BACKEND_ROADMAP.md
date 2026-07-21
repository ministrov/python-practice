# Дорожная карта изучения Python (3.12+)

## От Junior до Senior Backend Developer

> **Старт:** 2026-06-06
> **Последний чекпойнт:** 2026-07-14 (сеанс 14)
> **Прогресс:** Junior Level, Блок 2.3 завершён (ждёт финальную оценку); Блок 2.4 (Модули, файлы и дата/время), темы 1 (модули) и 3 (дата и время) завершены 8/8 каждая (2026-07-13, 2026-07-14), тема 2 (файлы продвинуто) пропущена и ждёт возврата; Блок 2.7 (Ошибки и исключения), тема 1 (try/except основы) завершена 8/8 — ВНЕ ОЧЕРЕДИ, на паузе; 2.5/2.6 не начаты
> **Длительность:** 18–24 месяца при 10–15 часах в неделю
> **Формат:** комбинированный — уровни (Junior → Middle → Senior) × темы × сроки
> **Стек-ориентир:** Python 3.12+, FastAPI/Django, PostgreSQL, SQLAlchemy, Redis, Docker, Kubernetes

---

## Содержание

1. [Введение и принципы обучения](#часть-1-введение-и-принципы-обучения)
2. [Уровень Junior (4–6 месяцев)](#часть-2-уровень-junior-46-месяцев)
3. [Уровень Middle (8–10 месяцев)](#часть-3-уровень-middle-810-месяцев)
4. [Уровень Senior (6–8+ месяцев)](#часть-4-уровень-senior-68-месяцев-и-далее-непрерывно)
5. [Чек-листы самопроверки](#часть-5-чек-листы-самопроверки)
6. [Полезные ссылки](#часть-6-полезные-ссылки)

---

## Часть 1. Введение и принципы обучения

### Как пользоваться планом

- Иди по уровням последовательно. Не перепрыгивай — пробелы в фундаменте всплывают на собеседованиях и в продакшене.
- Для каждого блока: **теория → практика → рефлексия**. Прочитал → написал код → объяснил вслух или в заметках, что понял.
- После каждой темы — **минимум 1 микро-задача** (10–30 минут кодинга).
- После каждого блока — **мини-проект** или существенное расширение текущего pet-проекта.
- Веди дневник: что изучил, что осталось непонятным, какие вопросы возникли. Через месяц возвращайся к непонятному — обычно становится ясно.
- Бэкенд — это не только язык. Параллельно с Python подтягивай **SQL, сети, Linux, Git** — без них синьором не стать.

> **🔴 ВАЖНО: ОЦЕНОЧНОЕ ТЕСТИРОВАНИЕ ПЕРЕД КАЖДОЙ НОВОЙ ТЕМОЙ**
>
> Перед переходом к следующему блоку:
>
> 1. **Микровопросы** (8–10 вопросов на микроблоки текущей темы) — убедиться, что понимаешь детали
> 2. **Финальная оценка** (4 задания на комбинацию знаний) — проверить готовность к следующему уровню
> 3. **Критерий успеха:** ≥ 80% правильных ответов → переход на следующий блок; < 80% → повтор конкретной части
>
> Это долговременное запоминание через активное припоминание + проверка пробелов.

### Где искать ответы

- **Официальная документация Python** (docs.python.org) — первоисточник по языку и stdlib
- **Real Python** (realpython.com) — лучшие практические туториалы по Python
- **PEP-ы** (peps.python.org) — Python Enhancement Proposals, как устроены и куда движутся фичи языка
- **FastAPI / Django docs** — официальные доки фреймворков, очень хорошего качества
- **PostgreSQL docs** — первоисточник по самой популярной БД для бэкенда
- **CPython source & devguide** (github.com/python/cpython) — внутренности интерпретатора

### Принципы самооценки

После каждого крупного блока пройди соответствующий [чек-лист](#часть-5-чек-листы-самопроверки). Если можешь без подсказок объяснить тему другу/коллеге/себе вслух — значит понял. Если не можешь — вернись и доучи.

---

## Часть 2. УРОВЕНЬ JUNIOR (4–6 месяцев)

**Цель уровня:** уверенно писать идиоматичный Python, понимать модель данных языка, работать с SQL и ORM, поднять простой REST API с базой данных и тестами.

### Блок 2.1. Фундамент языка (3–4 недели) ✅ ЗАВЕРШЕН

- [x] Типы данных: `int`, `float`, `bool`, `str`, `bytes`, `None`; изменяемые vs неизменяемые ✅
  - Файлы: `01_types_demo.py`, `02_types_task.py`
- [x] Переменные (объявление, изменение, именование) ✅ **ВЫДЕЛЕНО (15.06.2026)**
  - Новый файл: `03_variables_demo.py`, `03b_variables_task.py`
- [x] Ссылки и объекты: `id()`, `is` vs `==`, интернирование ✅ **ДОПОЛНЕНО (15.06.2026)**
  - Новые файлы: `03c_references_and_objects_demo.py`, `03c_references_and_objects_task.py`
- [x] Операторы: арифметические (`/`, `//`, `%`, базовые) ✅
- [x] Условия: `if/elif/else`, тернарное выражение ✅, `match/case` (structural pattern matching, 3.10+ — ✅ сделано)
- [x] Циклы: `for`, `while`, `break`/`continue`/`else`, `range`, `enumerate`, `zip` ✅
- [x] f-строки, форматирование, многострочные строки, основные методы `str` (демо + 12 практических задач) ✅
- [x] Ввод/вывод, работа с файлами через `with` (контекстные менеджеры на пользовательском уровне) ✅

> **Статус:** ✅ ЗАВЕРШЕН (18.06.2026). Все 7 тем закрыты. Финальная оценка пройдена.
> **Переход на блок 2.2 начат с 18.06.2026.**

### Блок 2.2. Структуры данных (2–3 недели) ✅ ЗАВЕРШЕН (2026-06-26)

- [x] **`list`**: срезы, методы, сортировка с `key`, list comprehensions ✅ (завершено 2026-06-18)
  - Файлы: `01_list_demo.py`, `02_list_task.py` (8/8 заданий)
- [x] **`tuple`**, распаковка, именованные кортежи ✅ (завершено 2026-06-18)
  - Файлы: `03_tuple_demo.py`, `04_tuple_task.py` (8/8 заданий)
- [x] **`dict`**: методы, dict comprehensions, `.get`/`.setdefault`, порядок вставки (3.7+) ✅ (завершено 2026-06-19)
  - Файлы: `05_dict_demo.py`, `06_dict_task.py` (8/8 заданий)
  - Микро-тест: 7/8 = 87.5% ✓ PASS
- [x] **`set` / `frozenset`**: операции над множествами, дедупликация ✅ (завершено 2026-06-26)
  - Файлы: `07_set_demo.py` ✅, `08_set_task.py` ✅ (8/8 заданий)
- [x] List/Dict/Set comprehensions — углубленно ✅ (завершено 2026-06-26)
  - Файлы: `09_list_comprehensions_demo.py` ✅, `10_list_comprehensions_task.py` ✅ (8/8 заданий)
- [x] Выбор структуры под задачу ✅ (завершено 2026-06-26)
  - Файлы: `11_choosing_structures_demo.py` ✅, `12_choosing_structures_task.py` ✅ (8/8 заданий)
- [ ] **Финальная оценка блока 2.2** — запланирована на 2026-06-27
- [ ] `collections`: `defaultdict`, `Counter`, `deque`, `OrderedDict` (дополнительно, если потребуется)
- [ ] Генераторные выражения vs списки — память и ленивость (дополнительно, если потребуется)

### Блок 2.3. Функции (2–3 недели) 🔄 В ПРОЦЕССЕ (сеанс 11: 2026-07-09)

- [x] Объявление, позиционные и именованные аргументы, значения по умолчанию (ловушка mutable default!) ✅ (2026-06-29)
  - Файлы: `01_functions_basics_demo.py`, `02_functions_basics_task.py` (8/8 заданий)
- [x] `*args`, `**kwargs`, positional-only `/` и keyword-only `*` параметры ✅ (2026-07-03)
  - Файлы: `03_args_kwargs_demo.py`, `04_args_kwargs_task.py` (8/8 заданий)
- [x] Области видимости: LEGB, `global`, `nonlocal`, замыкания ✅ (2026-07-06)
  - Файлы: `05_legb_demo.py`, `06_legb_task.py` (8/8 заданий, микро-тест 100%)
- [x] Функции как объекты первого класса, передача функций как значений ✅ (2026-07-06)
  - Файлы: `07_functions_as_objects_demo.py`, `08_functions_as_objects_task.py` (8/8 заданий)
- [x] Lambda, `map`/`filter`/`sorted` с ключами (но предпочитать comprehensions) ✅ (2026-07-06, в теме выше)
- [x] Ловушка "ссылка на функцию vs вызов функции" — закрепление ✅ (2026-07-09, мини-тест 5/5)

### Блок 2.4. Модули, файлы и дата/время (1–2 недели) 🔄 В ПРОЦЕССЕ (темы 1 и 3 завершены, тема 2 пропущена и ждёт возврата; сеанс 14: 2026-07-14)

- [x] Модули: `import`, `from ... import`, `as`; что происходит при импорте своего модуля ✅ (2026-07-13)
  - Файлы: `01_modules_demo.py` ✅, `02_modules_task.py` ✅ (8/8 заданий)
- [x] `if __name__ == "__main__"` — зачем нужен, разница между запуском файла и импортом ✅ (2026-07-13, в теме выше)
- [x] Пакеты: `__init__.py`, абсолютные vs относительные импорты, структура проекта ✅ (2026-07-13, в теме выше)
- [x] Поиск модулей: `sys.path`, порядок поиска (обзорно) ✅ (2026-07-13, в теме выше)
- [ ] Работа с файлами продвинуто: `pathlib.Path` вместо строк-путей, обход директорий
- [ ] Структурированные форматы: `csv`, `json` — чтение и запись
- [ ] Бинарные файлы, кодировки (`encoding=`), типичные ошибки (`UnicodeDecodeError`)
- [x] Дата и время: `datetime`, `date`, `time`, `timedelta` ✅ (2026-07-14)
  - Файлы: `05_datetime_demo.py` ✅, `06_datetime_task.py` ✅ (8/8 заданий)
- [x] Форматирование дат: `strftime`/`strptime`, ISO-формат ✅ (2026-07-14, в теме выше)
- [x] Часовые пояса — обзорно (`zoneinfo`) ✅ (2026-07-14, в теме выше)

### Блок 2.5. ООП и модель данных (3 недели) 🔄 В ПРОЦЕССЕ (сеанс 15: 2026-07-20, начат внепланово, долги по 2.2/2.3/2.4/2.7 отложены на 2026-07-24)

- [x] Классы, `__init__`, атрибуты экземпляра vs класса, `self` (2026-07-21)
- [x] Методы: обычные, `@classmethod`, `@staticmethod`, `@property` (геттеры/сеттеры) (2026-07-21)
- [ ] Наследование, `super()`, MRO (method resolution order) поверхностно
- [ ] Dunder-методы: `__repr__`, `__str__`, `__eq__`, `__hash__`, `__len__`, `__iter__`
- [ ] `dataclasses` — основной инструмент для классов-данных
- [ ] Композиция vs наследование — концепция
- [ ] `Enum`, `IntEnum`, `StrEnum` (3.11+)

### Блок 2.6. Типизация и качество кода (2 недели)

- [ ] Аннотации типов: `list[int]`, `dict[str, int]`, `Optional`/`| None`, `Union`/`|`
- [ ] `typing`: `Any`, `Callable`, `Iterable`, `Sequence`, `TypedDict`
- [ ] Проверка типов: `mypy` или `pyright` — настройка и запуск
- [ ] PEP 8, форматирование: `ruff` / `black`, линтинг `ruff`
- [ ] Виртуальные окружения: `venv`, управление зависимостями (`pip`, `requirements.txt`, или `uv`/`poetry`)

### Блок 2.7. Ошибки, исключения, стандартная библиотека (2 недели) 🔄 В ПРОЦЕССЕ, НА ПАУЗЕ (сеанс 12: 2026-07-09, начат внепланово до 2.4/2.5/2.6)

- [x] `try/except/else/finally`, иерархия исключений, свои классы исключений ✅ (2026-07-09)
  - Файлы: `01_exceptions_basics_demo.py` ✅, `02_exceptions_basics_task.py` ✅ (8/8 заданий)
- [ ] `raise`, `raise from`, exception chaining; `ExceptionGroup`/`except*` (3.11+)
- [ ] Контекстные менеджеры: `with`, `contextlib.contextmanager`
- [ ] Полезное из stdlib: `json`, `re`, `os`/`sys`, `itertools`, `functools` (`pathlib`/`datetime` — см. Блок 2.4)
- [ ] `logging` базово: уровни, форматтеры, хендлеры (вместо `print`)

### Блок 2.8. Базы данных и SQL — основы (3 недели)

- [ ] Реляционная модель: таблицы, строки, ключи (PK/FK), нормализация (1NF–3NF на пальцах)
- [ ] SQL: `SELECT`, `WHERE`, `JOIN` (inner/left), `GROUP BY`, `ORDER BY`, `LIMIT`
- [ ] `INSERT`/`UPDATE`/`DELETE`, транзакции, `COMMIT`/`ROLLBACK` базово
- [ ] PostgreSQL: установка, `psql`, основные типы данных
- [ ] Python + БД: `psycopg`, затем ORM — SQLAlchemy 2.0 (core + ORM, declarative)
- [ ] Миграции: Alembic — autogenerate, upgrade/downgrade

### Блок 2.9. Введение во фреймворк — FastAPI (3–4 недели)

- [ ] HTTP-основы: методы (GET/POST/PUT/PATCH/DELETE), статус-коды, заголовки, тело
- [ ] REST: ресурсы, идемпотентность, структура URL
- [ ] FastAPI: роуты, path/query параметры, request body
- [ ] Pydantic v2: модели, валидация, сериализация, `BaseSettings` для конфигурации
- [ ] Dependency Injection (`Depends`), обработка ошибок, статус-коды
- [ ] Подключение БД (SQLAlchemy), CRUD-эндпоинты, автодокументация (Swagger/OpenAPI)

### Блок 2.10. Git и инструменты (2 недели, параллельно)

- [ ] Git: `commit`, `branch`, `merge`, `rebase`, разрешение конфликтов, pull requests
- [ ] Командная строка / терминал Linux: навигация, права, пайпы, переменные окружения
- [ ] Отладка: `pdb`/`breakpoint()`, дебаггер в IDE (VS Code / PyCharm)
- [ ] REST-клиенты: `httpx`/`requests`, тестирование API через Postman/Insomnia/curl

### Pet-проекты Junior

1. **CLI-приложение** (например, менеджер задач или парсер) — аргументы, файлы, обработка ошибок
2. **REST API «To-do»** на FastAPI + SQLite/PostgreSQL — CRUD, валидация Pydantic, миграции Alembic
3. **API-агрегатор** — тянет данные из публичного API (`httpx`), кэширует, отдаёт через свои эндпоинты

### Книги и ресурсы Junior

- **Python Crash Course** (Eric Matthes) — для самого старта
- **Automate the Boring Stuff with Python** (Al Sweigart) — бесплатно онлайн, практика stdlib
- **Official Python Tutorial** (docs.python.org/3/tutorial) — справочник
- **Real Python** — статьи по каждой теме блоков выше
- **FastAPI docs** (fastapi.tiangolo.com) — официальный туториал, один из лучших в индустрии

### Критерии перехода на Middle

- Пишет идиоматичный Python без копирования из туториалов (comprehensions, контекстные менеджеры, dataclasses)
- Понимает разницу `is`/`==`, mutable/immutable, и ловушку mutable default arguments
- Уверенно пишет SQL с JOIN-ами и понимает, какой запрос генерирует ORM
- Сделал 2–3 законченных pet-проекта, один — REST API с БД
- Покрыл код хотя бы базовыми тестами на pytest

---

## Часть 3. УРОВЕНЬ MIDDLE (8–10 месяцев)

**Цель уровня:** проектировать сервисы, понимать внутренности языка и асинхронность, писать надёжный типизированный код, работать с очередями/кэшем, тестировать, контейнеризировать и деплоить.

### Блок 3.1. Глубокий Python (4–5 недель)

- [ ] Модель данных детально: что такое объект, `__dict__`, `__slots__` (память и скорость)
- [ ] Дескрипторы: `__get__`/`__set__`/`__delete__`, как работают `property` и методы под капотом
- [ ] Итераторы и генераторы: протокол итерации, `yield`, `yield from`, ленивые пайплайны
- [ ] Корутины-генераторы, `send`/`throw`/`close` (для понимания истоков async)
- [ ] Менеджеры контекста: класс с `__enter__`/`__exit__`, `contextlib` (`ExitStack`, `suppress`)
- [ ] Декораторы продвинуто: с состоянием, классы-декораторы, `functools.lru_cache`, `cache`, `singledispatch`
- [ ] Метаклассы и `__init_subclass__`, `__set_name__` — на уровне понимания, когда вообще нужны
- [ ] Дзен Python и идиоматичность (PEP 20)

### Блок 3.2. Асинхронность и конкурентность (4–5 недель)

- [ ] GIL: что это, что блокирует, как влияет на CPU- vs IO-bound задачи
- [ ] Потоки (`threading`), процессы (`multiprocessing`), `concurrent.futures` (`ThreadPoolExecutor`/`ProcessPoolExecutor`)
- [ ] `asyncio`: event loop, корутины, `async`/`await`, `await`-able объекты
- [ ] Задачи: `asyncio.create_task`, `gather`, `wait`, `TaskGroup` (3.11+), отмена и таймауты
- [ ] Асинхронный IO: `httpx`, async-драйверы БД (`asyncpg`, async SQLAlchemy)
- [ ] Типичные ошибки: блокирующий код в event loop, забытый `await`, race conditions
- [ ] Когда что: threads vs processes vs asyncio (карта применимости)

### Блок 3.3. Типизация на продвинутом уровне (3–4 недели)

- [ ] Generics: `TypeVar`, `Generic`, bounds и constraints; синтаксис дженериков 3.12 (`class Foo[T]`)
- [ ] `Protocol` (структурная типизация / duck typing с проверкой типов)
- [ ] `Literal`, `Final`, `overload`, `TypedDict` (total/NotRequired), `ParamSpec`, `Concatenate`
- [ ] `Annotated`, `NewType`, `TypeAlias`, `Self` (3.11+)
- [ ] Narrowing, `typing.cast`, `assert_type`, type guards (`TypeGuard`/`TypeIs`)
- [ ] Строгая конфигурация mypy/pyright (`strict`), постепенная типизация легаси
- [ ] Best practices: избегать `Any`, предпочитать `Protocol` наследованию

### Блок 3.4. Веб-фреймворки глубоко (5–6 недель)

> Выбери основной фреймворк под цель: **FastAPI** (API/микросервисы) или **Django** (монолит, админка, batteries-included). Желательно знать оба обзорно.

- [ ] FastAPI: продвинутый DI, middleware, фоновые задачи, lifespan, роутеры и версионирование
- [ ] Pydantic v2 глубоко: валидаторы, сериализация, settings, кастомные типы, производительность
- [ ] Аутентификация/авторизация: JWT, OAuth2 password/authorization code flow, scopes, RBAC
- [ ] Django: ORM, миграции, admin, DRF (Django REST Framework), сигналы, middleware
- [ ] ASGI vs WSGI — модель исполнения, серверы (`uvicorn`, `gunicorn`, `hypercorn`)
- [ ] Обработка ошибок, валидация, пагинация, фильтрация, rate limiting
- [ ] WebSocket, Server-Sent Events базово

### Блок 3.5. Базы данных глубоко (4–5 недель)

- [ ] SQLAlchemy 2.0 продвинуто: relationships, lazy/eager loading, N+1 проблема и её решение
- [ ] Транзакции и изоляция: уровни (read committed, repeatable read, serializable), deadlocks
- [ ] Индексы: B-tree, частичные, составные, покрывающие; когда индекс не используется
- [ ] `EXPLAIN`/`EXPLAIN ANALYZE` — чтение плана запроса, оптимизация
- [ ] Продвинутый SQL: оконные функции, CTE (`WITH`), подзапросы, агрегаты
- [ ] Connection pooling (PgBouncer / пул SQLAlchemy)
- [ ] NoSQL базово: Redis (структуры, TTL, использование как кэш), знакомство с MongoDB
- [ ] Миграции в проде: безопасные паттерны (zero-downtime, backfill)

### Блок 3.6. Тестирование (3–4 недели)

- [ ] `pytest`: фикстуры, параметризация, маркеры, conftest, scopes
- [ ] Мокинг: `unittest.mock`, `monkeypatch`, мок внешних HTTP (`respx`/`responses`)
- [ ] Тестирование API: `TestClient`/`httpx.AsyncClient`, тестовая БД (transactional fixtures)
- [ ] Покрытие: `coverage`/`pytest-cov` — что и как мерить, не гнаться за 100%
- [ ] Property-based тесты: `hypothesis` (введение)
- [ ] Фабрики данных: `factory_boy`/`faker`, изоляция тестов
- [ ] Пирамида тестирования: unit / integration / e2e — баланс

### Блок 3.7. Очереди, кэш, фоновые задачи (3 недели)

- [ ] Зачем фоновые задачи и брокеры сообщений
- [ ] Celery (+ Redis/RabbitMQ) или ARQ/Dramatiq/TaskIQ — задачи, ретраи, расписания (beat)
- [ ] Идемпотентность задач, обработка падений, dead letter queue
- [ ] Кэширование: Redis-паттерны (cache-aside, write-through), инвалидация, TTL
- [ ] RabbitMQ / Kafka — концепции pub/sub, consumer groups (обзорно)

### Блок 3.8. DevOps для бэкендера (4 недели)

- [ ] Docker: образы, слои, `Dockerfile` (multi-stage), `.dockerignore`, оптимизация размера
- [ ] Docker Compose: поднять стек (app + Postgres + Redis) локально
- [ ] Переменные окружения, секреты, 12-factor app
- [ ] CI/CD: GitHub Actions — линт, типы, тесты, сборка образа, деплой
- [ ] Линукс для бэкендера: процессы, systemd, логи, права, сеть (порты, `ss`/`netstat`)
- [ ] Nginx как reverse proxy базово
- [ ] Деплой: VPS вручную, затем PaaS (Railway/Render/Fly.io) или облако

### Pet-проекты Middle

1. **Полноценный REST API сервис** на FastAPI + async SQLAlchemy + PostgreSQL: аутентификация (JWT), RBAC, пагинация, тесты, Docker Compose
2. **Сервис с фоновыми задачами**: загрузка/обработка файлов или рассылка через Celery + Redis
3. **Реал-тайм сервис** на WebSocket (чат или нотификации) с хранением истории
4. **Микросервис + интеграция**: два сервиса общаются через HTTP/очередь, с CI и контейнеризацией

### Книги и ресурсы Middle

- **Fluent Python** (Luciano Ramalho), 2-е издание — главная книга про идиоматичный Python
- **Architecture Patterns with Python** (Percival, Gregory) — DDD, репозитории, сервисный слой (бесплатно онлайн)
- **Robust Python** (Patrick Viafore) — типизация и надёжный код
- **Designing Data-Intensive Applications** (Martin Kleppmann) — начать читать (БД, очереди, распределённость)
- **High Performance Django** / **FastAPI docs (Advanced)** — продвинутые разделы фреймворков
- **PostgreSQL docs** + **Use The Index, Luke** (use-the-index-luke.com) — индексы и производительность

### Критерии перехода на Senior

- Может в одиночку поднять сервис с нуля: API, БД, миграции, тесты, Docker, CI
- Понимает GIL, разницу async/threads/processes и осознанно выбирает модель под задачу
- Уверенно типизирует сложные кейсы, читает чужие типы, настраивает strict mypy
- Чинит N+1, читает `EXPLAIN ANALYZE`, оптимизирует запросы
- Понимает trade-offs архитектурных решений и умеет их аргументированно обсуждать
- Может провести code review и обосновать каждое замечание

---

## Часть 4. УРОВЕНЬ SENIOR (6–8 месяцев и далее непрерывно)

**Цель уровня:** проектировать архитектуру распределённых систем, принимать технические решения, обеспечивать надёжность и наблюдаемость, оптимизировать, менторить, влиять на процессы команды.

### Блок 4.1. Внутренности CPython (4–5 недель)

- [ ] Модель исполнения: компиляция в bytecode, `dis`, frame objects, оценочный цикл
- [ ] Управление памятью: reference counting + cyclic GC (generations), `gc` модуль
- [ ] GIL детально: почему существует, как влияет, эксперименты с no-GIL/free-threaded (PEP 703, 3.13+)
- [ ] Объектная модель в C: PyObject, как устроены int/list/dict под капотом
- [ ] Оптимизации интерпретатора: specializing adaptive interpreter (3.11+), JIT (3.13+, экспериментально)
- [ ] Профилирование: `cProfile`, `py-spy`, `scalene`, чтение flame graphs
- [ ] Альтернативы: PyPy, расширения на C/Cython/Rust (PyO3) — когда оправдано

### Блок 4.2. Performance и масштабирование (5–6 недель)

- [ ] Профилирование CPU и памяти, поиск узких мест (`py-spy`, `memray`, `tracemalloc`)
- [ ] Оптимизация БД: партиционирование, репликация (read replicas), шардирование (концепции)
- [ ] Кэширование на всех уровнях: app, Redis, CDN; стратегии инвалидации
- [ ] Асинхронная обработка и батчинг, backpressure
- [ ] Connection pooling, тюнинг воркеров (gunicorn/uvicorn), таймауты
- [ ] Нагрузочное тестирование: `locust`, `k6`; SLA/SLO, percentile latency (p95/p99)
- [ ] Векторизация и обработка данных: `numpy`/`polars` где уместно

### Блок 4.3. Архитектура и проектирование (5–6 недель)

- [ ] SOLID, DRY, KISS применительно к бэкенду
- [ ] Чистая архитектура / Hexagonal (ports & adapters) / DDD: слои, репозитории, use cases
- [ ] Монолит vs микросервисы — когда что, decomposition strategies
- [ ] Паттерны интеграции: API Gateway, BFF, service mesh (обзорно)
- [ ] Событийная архитектура: event-driven, CQRS, event sourcing, saga, outbox pattern
- [ ] Паттерны проектирования (GoF) в Python: Strategy, Factory, Adapter, Observer, Repository, Unit of Work
- [ ] Идемпотентность, exactly-once vs at-least-once, distributed transactions

### Блок 4.4. Распределённые системы и надёжность (4–5 недель)

- [ ] CAP-теорема, consistency models (eventual/strong), кворумы
- [ ] Брокеры сообщений глубоко: Kafka (партиции, offset, consumer groups), RabbitMQ exchange-типы
- [ ] Resilience: retries с backoff, circuit breaker, bulkhead, timeout, graceful degradation
- [ ] Распределённые блокировки, leader election (Redis/etcd/ZooKeeper концептуально)
- [ ] Согласованность данных между сервисами: saga, outbox, CDC (Debezium обзорно)
- [ ] Rate limiting и throttling (token bucket, sliding window)

### Блок 4.5. Observability и эксплуатация (4 недели)

- [ ] Логирование структурированное (JSON), correlation/trace id, агрегация (ELK/Loki)
- [ ] Метрики: Prometheus + Grafana, RED/USE методологии, алертинг
- [ ] Distributed tracing: OpenTelemetry, Jaeger/Tempo
- [ ] Health checks, readiness/liveness probes, graceful shutdown
- [ ] Incident management: on-call, post-mortem, runbooks
- [ ] Feature flags, прогрессивные релизы (canary, blue-green)

### Блок 4.6. Инфраструктура и облако (4–5 недель)

- [ ] Kubernetes: pods, deployments, services, ingress, configmaps/secrets, HPA
- [ ] Helm / Kustomize базово; деплой Python-сервиса в k8s
- [ ] IaC: Terraform базово
- [ ] Облака: AWS/GCP основные сервисы (compute, managed Postgres, S3-совместимое хранилище, queues)
- [ ] CI/CD продвинуто: пайплайны, окружения (dev/staging/prod), стратегии деплоя, rollback
- [ ] Стоимость и capacity planning

### Блок 4.7. Безопасность (3 недели)

- [ ] OWASP Top 10 для API/бэкенда: injection (SQL), broken auth, BOLA/IDOR, SSRF, mass assignment
- [ ] Безопасная аутентификация: хеширование паролей (argon2/bcrypt), сессии vs JWT, refresh-токены
- [ ] OAuth 2.0 / OpenID Connect глубоко, scopes, PKCE
- [ ] Управление секретами: Vault, KMS, ротация; защита от утечек в репозитории
- [ ] Валидация и санитизация входных данных, защита от инъекций
- [ ] Аудит зависимостей: `pip-audit`, Dependabot/Renovate, SBOM; supply chain
- [ ] TLS, шифрование данных at-rest и in-transit, PII и комплаенс (GDPR базово)

### Блок 4.8. Soft skills и процессы (постоянно)

- [ ] Code review: как давать конструктивные замечания и принимать критику
- [ ] Менторство джунов и мидлов
- [ ] RFC / ADR (Architecture Decision Records) — писать и читать
- [ ] Технические собеседования с обеих сторон стола (system design в т.ч.)
- [ ] Эстимация задач, декомпозиция, переговоры о scope
- [ ] Документация: README, ARCHITECTURE.md, ADR, runbooks, OpenAPI как контракт

### Блок 4.9. Спецификация и тренды (постоянно)

- [ ] Чтение PEP-ов (выборочно: data model, typing, async)
- [ ] Следить за релизами CPython (что нового в 3.13/3.14: free-threading, JIT)
- [ ] Подписки: Python Weekly, PyCoder's Weekly, релиз-ноуты FastAPI/Django/SQLAlchemy
- [ ] Конференции: PyCon, EuroPython (доклады на YouTube)

### Pet-проекты Senior

1. **Распределённая система из нескольких сервисов**: event-driven через Kafka/RabbitMQ, outbox/saga, идемпотентность
2. **Сервис с полной observability**: метрики (Prometheus), трейсинг (OpenTelemetry), структурные логи, дашборды Grafana
3. **Деплой в Kubernetes**: Helm-чарт, HPA, health checks, CI/CD с canary-релизом
4. **Высоконагруженный компонент**: оптимизация под нагрузку с профилированием, нагрузочными тестами и отчётом p95/p99
5. **Вклад в open-source** — patch / документация / issue в популярную библиотеку (FastAPI, SQLAlchemy, Pydantic, httpx, Celery)

### Книги и ресурсы Senior

- **Designing Data-Intensive Applications** (Martin Kleppmann) — must-read для понимания систем целиком
- **Database Internals** (Alex Petrov) — как устроены БД изнутри
- **Building Microservices** (Sam Newman), 2-е издание
- **Designing Distributed Systems** (Brendan Burns)
- **Site Reliability Engineering** (Google) — бесплатно онлайн
- **The Pragmatic Programmer** (David Thomas, Andrew Hunt) — 20-th anniversary edition
- **CPython Internals** (Anthony Shaw) + **python devguide** (devguide.python.org)

---

## Часть 5. Чек-листы самопроверки

> Отмечай галочки в чек-листах внутри каждого блока выше. Когда в текущем уровне отмечено **≥ 80%** пунктов и сделаны pet-проекты — можно двигаться на следующий уровень.

### Сводный чек-лист Junior → Middle

- [ ] Все блоки 2.1–2.10 пройдены (≥ 80% галочек)
- [ ] 2–3 pet-проекта Junior завершены и выложены на GitHub
- [ ] Прочитан Python Crash Course или Automate the Boring Stuff
- [ ] Пишу SQL с JOIN-ами и понимаю запросы ORM
- [ ] Уверенно использую Git и pytest

### Сводный чек-лист Middle → Senior

- [ ] Все блоки 3.1–3.8 пройдены (≥ 80% галочек)
- [ ] 3–4 pet-проекта Middle завершены (минимум один с Docker Compose и CI)
- [ ] Сервис задеплоен и доступен публично
- [ ] Настроен полный CI с линтом, типами (strict mypy), тестами
- [ ] Прочитаны Fluent Python и Architecture Patterns with Python

### Сводный чек-лист Senior (бесконечно развивается)

- [ ] Все блоки 4.1–4.9 пройдены (≥ 80% галочек)
- [ ] Внесён вклад в open-source
- [ ] Сервис развёрнут в Kubernetes с observability
- [ ] Написан хотя бы один RFC / ADR в реальной команде
- [ ] Менторил джуна / мидла (или провёл серию докладов)
- [ ] Прочитан Designing Data-Intensive Applications
- [ ] Регулярно слежу за релизами CPython и блогами

---

## Часть 6. Полезные ссылки

### Документация

- [docs.python.org](https://docs.python.org/3/) — официальная документация Python
- [FastAPI](https://fastapi.tiangolo.com/) — туториал и продвинутые разделы
- [Django docs](https://docs.djangoproject.com/) + [DRF](https://www.django-rest-framework.org/)
- [SQLAlchemy 2.0 docs](https://docs.sqlalchemy.org/)
- [Pydantic docs](https://docs.pydantic.dev/)
- [PostgreSQL docs](https://www.postgresql.org/docs/)

### Спецификации и внутренности

- [PEP Index](https://peps.python.org/) — все Python Enhancement Proposals
- [Python devguide](https://devguide.python.org/) — как устроен CPython
- [CPython на GitHub](https://github.com/python/cpython)
- [typing docs](https://typing.readthedocs.io/)

### Обучение и практика

- [Real Python](https://realpython.com/) — туториалы по всем темам
- [Use The Index, Luke](https://use-the-index-luke.com/) — индексы и SQL-производительность
- [Architecture Patterns with Python](https://www.cosmicpython.com/) — бесплатная книга онлайн
- [Test & Code](https://testandcode.com/) — про тестирование на Python
- [Exercism / LeetCode / Codewars](https://exercism.org/tracks/python) — задачи для практики

### Блоги и видео

- [Real Python](https://realpython.com/) — статьи и подкаст
- [Talk Python To Me](https://talkpython.fm/) — подкаст
- [mCoding (YouTube)](https://www.youtube.com/@mCoding) — глубокие разборы Python
- [ArjanCodes (YouTube)](https://www.youtube.com/@ArjanCodes) — дизайн и архитектура на Python
- [PyCon / EuroPython talks (YouTube)](https://www.youtube.com/@PyConUS)

### Рассылки

- Python Weekly
- PyCoder's Weekly
- Awesome Python (github.com/vinta/awesome-python)
- Console Weekly (для DevOps-инструментов)

### Сообщества

- Stack Overflow
- Reddit: r/Python, r/learnpython, r/django, r/flask
- Discord/Telegram сообщества Python, FastAPI
- Python Discord (pythondiscord.com)

---

**Удачи на пути!** Помни: 18–24 месяца — это ориентир. Кто-то управится быстрее, кому-то нужно больше. Бэкенд — это язык **плюс** базы данных, сети, инфраструктура и архитектура: не зацикливайся только на Python. Главное — стабильная практика и фокус на понимании, а не на скорости.
