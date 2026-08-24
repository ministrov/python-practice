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
