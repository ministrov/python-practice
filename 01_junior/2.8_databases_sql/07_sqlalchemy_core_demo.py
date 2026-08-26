# -*- coding: utf-8 -*-
"""
Блок 2.8, тема 4a: SQLAlchemy 2.0 — Core (слой запросов)
════════════════════════════════════════════════════════════════════════
Темы:
  0. Мост: зачем Core, если сырой SQL уже работает
  1. Engine — не то же самое, что Connection
  2. MetaData + Table — схема как Python-объекты, а не текст CREATE TABLE
  3. metadata.create_all() — создание таблиц
  4. insert() + engine.begin() — транзакция как контекстный менеджер
  5. select() + .where() — фильтрация без ручной склейки строки
  6. .join() — та же связка authors/posts, что и в психкопг-практике
  7. func.count() + .group_by() — агрегаты в Core
  8. Итог: Core vs сырой SQL, и куда дальше (ORM)

БД — тот же контейнер pg-learning (см. 05_postgres_basics_demo.py):
    host=localhost, port=5432, db=learning,
    user=learning, password=learning
"""

from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    create_engine,
    insert,
    select,
    func,
)

# ════════════════════════════════════════════════════════════════════════
# 0. Мост: зачем Core, если сырой SQL уже работает
# ════════════════════════════════════════════════════════════════════════
# Всё, что ты писал в 06_psycopg_practice.py, работает — но SQL там
# живёт как ТЕКСТ (строка). Компьютер не знает, что "authors.name" —
# это реальная колонка, пока строка не долетит до сервера. Опечатку
# (`authors_id` вместо `author_id`) ты нашёл только по ошибке psycopg
# в рантайме — Python до этого момента её не видел.
#
# Core решает ту же задачу — построить SQL-запрос, — но описывает его
# Python-ОБЪЕКТАМИ (Table, Column, select(), where()...), а не строкой.
# Финальный SQL Core соберёт сам. Выгода: автодополнение в редакторе,
# опечатки в именах колонок ловит Python (AttributeError), а не сервер
# в рантайме.
#
# Мнемоника: это как разница между f-строкой с ручной HTML-вёрсткой и
# built-in конструктором (`ET.Element(...)`) — второй не даст забыть
# закрыть тег, потому что тег вообще не текст, а объект.

# ════════════════════════════════════════════════════════════════════════
# 1. Engine — не то же самое, что Connection
# ════════════════════════════════════════════════════════════════════════
# psycopg.connect(...) даёт ОДНО соединение. create_engine(...) даёт
# ФАБРИКУ соединений с пулом — Engine сам открывает/переиспользует/
# закрывает физические соединения по мере надобности. Ты почти никогда
# не работаешь с Engine напрямую для запросов — только чтобы получить
# Connection (через .connect() или .begin()).
#
# Строка подключения (URL) — те же параметры, что были в psycopg.connect(),
# просто собранные в одну строку: dialect+driver://user:password@host:port/db

engine = create_engine(
    "postgresql+psycopg://learning:learning@localhost:5432/learning"
)

# ════════════════════════════════════════════════════════════════════════
# 2. MetaData + Table — схема как Python-объекты
# ════════════════════════════════════════════════════════════════════════
# MetaData — реестр всех таблиц, которые ты описал (пустой "каталог").
# Table — Python-описание ОДНОЙ таблицы: имя, колонки, типы, ключи.
# Сравни с CREATE TABLE authors (...) из 06_psycopg_practice.py — те же
# колонки, тот же смысл, но теперь это объект, а не текст запроса.

metadata = MetaData()

authors = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("author_id", Integer, ForeignKey("authors.id")),
    Column("published", Boolean, nullable=False, default=False),
)

# ════════════════════════════════════════════════════════════════════════
# 3. metadata.create_all() — создание таблиц
# ════════════════════════════════════════════════════════════════════════
# Один вызов создаёт ВСЕ таблицы, описанные в этом MetaData, в правильном
# порядке (authors раньше posts — Core сам видит ForeignKey и не пытается
# создать posts первой). Аналог твоих двух CREATE TABLE подряд.
#
# metadata.drop_all(engine) — обратная операция, аналог DROP TABLE.
# Тот же трюк, что и DROP TABLE IF EXISTS ... CASCADE в психкопг-практике:
# сначала дропаем, чтобы демо было безопасно перезапускать.

metadata.drop_all(engine)
metadata.create_all(engine)

# ════════════════════════════════════════════════════════════════════════
# 4. insert() + engine.begin() — транзакция как контекстный менеджер
# ════════════════════════════════════════════════════════════════════════
# engine.begin() открывает Connection И транзакцию сразу. При успешном
# выходе из `with` — автоматический commit(); при исключении внутри —
# автоматический rollback(). Это именно то поведение, которое ты уже
# видел у `with psycopg.connect(...) as conn:` (мост в
# PYTHON_DB_API_CHEATSHEET.md) — только на уровне ОДНОЙ транзакции,
# не всего соединения.

with engine.begin() as connection:
    connection.execute(
        insert(authors),
        [
            {"name": "Иван Петров"},
            {"name": "Мария Сидорова"},
            {"name": "Алексей Смирнов"},
        ],
    )
    connection.execute(
        insert(posts),
        [
            {"title": "Введение в SQL", "author_id": 1, "published": True},
            {"title": "Основы JOIN", "author_id": 1, "published": False},
            {"title": "Что такое ORM", "author_id": 2, "published": True},
            {"title": "Индексы", "author_id": 2, "published": True},
            {"title": "EXPLAIN ANALYZE", "author_id": 3, "published": False},
        ],
    )
# ← выход из `with` без ошибок = автоматический commit(), как и
#   cursor.executemany() + connection.commit() в психкопг-практике,
#   только commit теперь не нужно звать руками.

# ════════════════════════════════════════════════════════════════════════
# 5. select() + .where() — фильтрация без ручной склейки строки
# ════════════════════════════════════════════════════════════════════════
# select(authors) = "SELECT * FROM authors". .where(...) добавляет
# условие — сравнение делается прямо на объекте колонки Python-
# оператором (==, >, ...), а не текстом "WHERE name = ...".

with engine.connect() as connection:
    query = select(authors).where(authors.c.name == "Иван Петров")
    result = connection.execute(query)
    print(result.fetchall())
    # [(1, 'Иван Петров')]
    # authors.c.name — .c это "columns", доступ к колонке по имени.
    # Мнемоника: authors.c.name ~ authors["name"] в словарном мышлении,
    # только через атрибут, а не по строковому ключу.

# ════════════════════════════════════════════════════════════════════════
# 6. .join() — та же связка authors/posts, что и в психкопг-практике
# ════════════════════════════════════════════════════════════════════════
# select(...).join(...) собирает ровно тот же SQL, что ты писал руками:
#   FROM authors JOIN posts ON posts.author_id = authors.id WHERE ...
# Разница только в том, что ON-условие Core выводит САМ — по ForeignKey,
# который уже объявлен в Table posts (Column("author_id", ...,
# ForeignKey("authors.id"))). Явно передавать условие не обязательно,
# но можно — join(posts, posts.c.author_id == authors.c.id).

with engine.connect() as connection:
    query = (
        select(posts.c.title, authors.c.name)
        .join(authors)
        .where(posts.c.published)
    )
    result = connection.execute(query)
    print(result.fetchall())
    # [('Введение в SQL', 'Иван Петров'),
    #  ('Что такое ORM', 'Мария Сидорова'),
    #  ('Индексы', 'Мария Сидорова')]

# ════════════════════════════════════════════════════════════════════════
# 7. func.count() + .group_by() — агрегаты в Core
# ════════════════════════════════════════════════════════════════════════
# func — фабрика для вызова любой SQL-функции сервера (COUNT, SUM, AVG,
# ...). func.count(posts.c.id) = "COUNT(posts.id)" — то же самое, что
# ты написал руками в 06_psycopg_practice.py, только без риска
# опечатки в имени функции/колонки, невидимой для Python.

with engine.connect() as connection:
    query = (
        select(authors.c.name, func.count(posts.c.id))
        .join(posts)
        .group_by(authors.c.name)
    )
    result = connection.execute(query)
    print(result.fetchall())
    # [('Иван Петров', 2), ('Мария Сидорова', 2), ('Алексей Смирнов', 1)]
    # (порядок групп в выводе не гарантирован без ORDER BY)

# ════════════════════════════════════════════════════════════════════════
# 8. Итог: Core vs сырой SQL — и куда дальше
# ════════════════════════════════════════════════════════════════════════
# | Сырой SQL (psycopg)                          | Core                     |
# |-----------------------------------------------|--------------------------|
# | connection = psycopg.connect(...)              | engine = create_engine(...) |
# | cursor.execute("SELECT ...")                   | connection.execute(select(...)) |
# | "WHERE name = %s", (value,)                    | .where(authors.c.name == value) |
# | "JOIN posts ON posts.author_id = authors.id"   | .join(authors)  # по ForeignKey |
# | "GROUP BY authors.name" + "COUNT(posts.id)"    | .group_by(...) + func.count(...) |
#
# Core — это ещё не ORM. Здесь нет классов Author/Post — есть только
# Table-объекты и обычные кортежи в результате (Row), как у psycopg.
# СЛЕДУЮЩИЙ ШАГ — ORM: классы вместо Table (похожие на dataclass из
# блока 2.5), Session вместо Connection, и объекты вместо кортежей в
# результате запроса.
