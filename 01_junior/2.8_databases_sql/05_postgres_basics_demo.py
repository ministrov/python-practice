# -*- coding: utf-8 -*-
"""
Блок 2.8.3: Демо — PostgreSQL, psql, основные типы данных
════════════════════════════════════════════════════════════════════════
PostgreSQL здесь поднят в Docker-контейнере, а не установлен в систему
напрямую — так проще: одна команда `docker rm -f pg-learning` убирает
БД с машины полностью, ничего не остаётся в реестре/автозапуске.

Подключение (пригодится дальше для psycopg):
    host=localhost, port=5432, db=learning,
    user=learning, password=learning

Темы:
  0. Как поднят контейнер (справочно, не выполняется здесь)
  1. psql — основные мета-команды (\\dt, \\d, \\c, \\q)
  2. Типы данных: SERIAL, VARCHAR(n), NUMERIC(p,s), BOOLEAN, TIMESTAMP
  3. Чем это отличается от sqlite3, с которым ты уже работал
"""

import subprocess

# ════════════════════════════════════════════════════════════════════════
# 0. Как поднят контейнер (справочно — уже выполнено, повторно не нужно)
# ════════════════════════════════════════════════════════════════════════
# docker run -d --name pg-learning \
#   -e POSTGRES_USER=learning \
#   -e POSTGRES_PASSWORD=learning \
#   -e POSTGRES_DB=learning \
#   -p 5432:5432 \
#   -v pg-learning-data:/var/lib/postgresql/data \
#   postgres:16
#
# -v создаёт именованный volume — данные переживут `docker stop` и
# перезапуск контейнера (но не `docker rm -v` с явным удалением тома).
# Если контейнер уже существует, но остановлен: `docker start pg-learning`.


def run_psql(command: str) -> str:
    """Выполнить SQL или psql-мета-команду в контейнере pg-learning.

    -c принимает и обычный SQL, и одиночную мета-команду вида \\dt —
    оба варианта ведут себя так же, как если бы их ввели в интерактивной
    psql-сессии. encoding="utf-8" — иначе на Windows subprocess декодирует
    вывод контейнера (он всегда в UTF-8) в кодировке консоли и кириллица
    превращается в кракозябры. Уведомления psql (например, "Did not find
    any relations" у пустого \\dt) идут в stderr, а не в stdout — поэтому
    возвращаем оба потока вместе.
    """
    result = subprocess.run(
        [
            "docker", "exec", "pg-learning",
            "psql", "-U", "learning", "-d", "learning", "-c", command,
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    return result.stdout + result.stderr


# ════════════════════════════════════════════════════════════════════════
# 1. psql — основные мета-команды
# ════════════════════════════════════════════════════════════════════════
# \dt        — список таблиц текущей БД (аналог SELECT name FROM
#              sqlite_master WHERE type='table' в sqlite3)
# \d table   — структура таблицы: столбцы, типы, PK, индексы
# \c dbname  — переключиться на другую базу внутри той же psql-сессии
# \q         — выйти из psql (только в интерактивном режиме)

print(run_psql(r"\dt"))
# Did not find any relations.
# (уведомление psql об отсутствии таблиц — не ошибка; таблиц пока нет)


# ════════════════════════════════════════════════════════════════════════
# 2. Типы данных: SERIAL, VARCHAR(n), NUMERIC(p,s), BOOLEAN, TIMESTAMP
# ════════════════════════════════════════════════════════════════════════

print(run_psql("""
    CREATE TABLE demo_types (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        price NUMERIC(10, 2) NOT NULL,
        in_stock BOOLEAN NOT NULL DEFAULT true,
        created_at TIMESTAMP NOT NULL DEFAULT now()
    );
"""))
# CREATE TABLE

print(run_psql(
    "INSERT INTO demo_types (name, price) VALUES ('Ноутбук', 79990.00);"
))
# INSERT 0 1

print(run_psql("SELECT * FROM demo_types;"))
#  id |  name   |  price   | in_stock |         created_at
# ----+---------+----------+----------+----------------------------
#   1 | Ноутбук | 79990.00 | t        | 2026-08-24 12:07:25.431115

print(run_psql(r"\d demo_types"))
#    Column   |            Type             | Nullable |    Default
# ------------+-----------------------------+----------+---------------
#  id         | integer                     | not null | nextval(...)
#  name       | character varying(50)       | not null |
#  price      | numeric(10,2)               | not null |
#  in_stock   | boolean                     | not null | true
#  created_at | timestamp without time zone | not null | now()


# ════════════════════════════════════════════════════════════════════════
# 3. Чем это отличается от sqlite3
# ════════════════════════════════════════════════════════════════════════
# SERIAL PRIMARY KEY
#   Вместо INTEGER PRIMARY KEY (auto-increment в sqlite3). Под капотом
#   создаёт отдельную последовательность (demo_types_id_seq), которая
#   генерирует следующий id — видно в выводе \d как nextval(...).
#
# VARCHAR(50)
#   Строка с ограничением длины. sqlite3 типы вообще не проверяет
#   строго ("type affinity" — особенность именно sqlite3, не
#   SQL-стандарта) — TEXT там без всяких ограничений.
#
# NUMERIC(10, 2)
#   Точное число с фиксированной точностью (10 знаков всего, 2 после
#   запятой) — для денег правильнее REAL/float, у которого есть
#   погрешности округления с плавающей точкой.
#
# BOOLEAN
#   Настоящий тип true/false. В sqlite3 булевых типов нет вообще,
#   используют 0/1.
#
# TIMESTAMP DEFAULT now()
#   Метка времени, now() — функция САМОЙ БД, вычисляется на сервере,
#   а не в Python.
#
# Сам SQL (SELECT/WHERE/JOIN/GROUP BY и т.д. из тем 1-2) работает в
# PostgreSQL практически без изменений — меняется в основном схема
# (типы данных при CREATE TABLE), а не синтаксис запросов.

print(run_psql("DROP TABLE demo_types;"))
# DROP TABLE
