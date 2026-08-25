# -*- coding: utf-8 -*-
"""
Блок 2.8: Свободная практика — psycopg + настоящий PostgreSQL
════════════════════════════════════════════════════════════════════════
Не формальное задание роадмапа — практика на живой учебной базе (та же
теория, что в темах 1-2, но на PostgreSQL вместо sqlite3, через
psycopg вместо sqlite3-модуля).

БД поднята в Docker-контейнере `pg-learning` (см. 05_postgres_basics_demo.py):
    host=localhost, port=5432, db=learning,
    user=learning, password=learning

Отличие psycopg от sqlite3, с которым ты уже работал:
    sqlite3.connect(":memory:")          psycopg.connect("...")
    connection.cursor()                  connection.cursor()
    cursor.execute(sql, params)          cursor.execute(sql, params)
    cursor.fetchall() / fetchone()       cursor.fetchall() / fetchone()
    connection.commit() / rollback()     connection.commit() / rollback()
API почти идентичен — оба следуют одному стандарту (PEP 249, Python
Database API). Именно поэтому переучиваться с sqlite3 на PostgreSQL
почти не пришлось для самого SQL.
"""

import psycopg

# ТВОЙ КОД ЗДЕСЬ:

connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="learning",
    user="learning",
    password="learning"
)

cursor = connection.cursor()
cursor.execute("SELECT version();")
result = cursor.fetchone()
print(result)

cursor.execute("DROP TABLE IF EXISTS posts, authors CASCADE")

cursor.execute("""
    CREATE TABLE authors (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE posts (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        author_id INTEGER REFERENCES authors(id),
        published BOOLEAN NOT NULL DEFAULT false
    )
""")

authors_data = [
    ("Иван Петров",),
    ("Мария Сидорова",),
    ("Алексей Смирнов",),
    ("Ольга Кузнецова",),
    ("Дмитрий Волков",),
    ("Екатерина Новикова",),
]

cursor.executemany(
    "INSERT INTO authors (name) VALUES (%s)",
    authors_data
)

posts_data = [
    ("Введение в SQL", 1, True),
    ("Основы JOIN", 1, False),
    ("Нормализация баз данных", 2, True),
    ("Транзакции и ACID", 2, False),
    ("Индексы и производительность", 3, True),
    ("Что такое ORM", 3, True),
    ("SQLite vs PostgreSQL", 3, False),
    ("Работа с JSONB в Postgres", 4, True),
    ("Оконные функции на практике", 4, False),
    ("Проектирование схемы БД", 5, True),
    ("Миграции и Alembic", 5, False),
    ("Репликация в PostgreSQL", 6, True),
    ("Бэкапы: pg_dump и восстановление", 6, True),
    ("EXPLAIN ANALYZE для новичков", 6, False),
]

cursor.executemany(
    "INSERT INTO posts (title, author_id, published) VALUES (%s, %s, %s)",
    posts_data
)

connection.commit()
cursor.execute("SELECT * FROM posts")
print(cursor.fetchall())

cursor.execute("""
    SELECT posts.title, authors.name 
    FROM authors
    INNER JOIN posts ON posts.author_id = authors.id
    WHERE posts.published 
""")

result = cursor.fetchall()
print(result)

# ════════════════════════════════════════════════════════════════════════
# GROUP BY + агрегат: количество постов у каждого автора (без WHERE —
# считаем все посты, не только опубликованные).
# ════════════════════════════════════════════════════════════════════════

cursor.execute("""
    SELECT authors.name, COUNT(posts.id) AS post_count
    FROM authors
    JOIN posts ON posts.author_id = authors.id
    GROUP BY authors.name
""")

result = cursor.fetchall()
print(result)
