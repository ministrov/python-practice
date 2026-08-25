# -*- coding: utf-8 -*-
"""
Блок 2.8, тема 4b: SQLAlchemy 2.0 — ORM
════════════════════════════════════════════════════════════════════════
Темы:
  0. Мост: ORM-класс ~ dataclass, только со "знанием" своей таблицы
  1. DeclarativeBase — общий предок всех моделей
  2. Mapped[...] + mapped_column() — колонки как типизированные поля
  3. relationship() — связь между моделями как обычный Python-атрибут
  4. Base.metadata.create_all() — создание таблиц (тот же вызов, что в Core)
  5. Session — session.add()/commit(), отличие от engine.begin()
  6. Запрос через select(Model) — результат: ОБЪЕКТЫ, не кортежи
  7. Доступ к relationship — author.posts без ручного JOIN
  8. select(Model.col, ...).join(...) — Core-запросы всё ещё доступны
  9. Итог: Core vs ORM

БД — тот же контейнер pg-learning (см. 05_postgres_basics_demo.py):
    host=localhost, port=5432, db=learning,
    user=learning, password=learning

Домен — authors/posts, тот же, что в 07_sqlalchemy_core_demo.py, чтобы
сравнение Core vs ORM было прямым: одна и та же схема, два способа с
ней работать.
"""

from typing import List

from sqlalchemy import ForeignKey, create_engine, func, select
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
    relationship,
)

# ════════════════════════════════════════════════════════════════════════
# 0. Мост: ORM-класс ~ dataclass, только со "знанием" своей таблицы
# ════════════════════════════════════════════════════════════════════════
# В блоке 2.5 ты писал так (09_dataclasses_demo.py):
#
#     @dataclass
#     class Author:
#         id: int
#         name: str
#
# Это просто класс с полями — он ничего не знает про базу данных.
# ORM-модель выглядит почти так же (аннотации типов на месте), но
# каждое поле — это Mapped[...] + mapped_column(), а класс наследуется
# от DeclarativeBase. Разница: этот класс ЗНАЕТ, в какую таблицу и как
# сохранять свои объекты. dataclass хранит данные в памяти, ORM-модель
# хранит данные в памяти И умеет сама себя сохранить в БД через Session.

# ════════════════════════════════════════════════════════════════════════
# 1. DeclarativeBase — общий предок всех моделей
# ════════════════════════════════════════════════════════════════════════
# Аналог того, что ты уже видел в блоке 2.5 (13_abstraction_demo.py) —
# общий базовый класс, от которого наследуются конкретные модели. Здесь
# он не абстрактный в смысле ABC, а служебный: именно через него
# SQLAlchemy узнаёт "какие классы вообще являются моделями таблиц".


class Base(DeclarativeBase):
    pass


# ════════════════════════════════════════════════════════════════════════
# 2-3. Mapped[...] + mapped_column() + relationship()
# ════════════════════════════════════════════════════════════════════════
# Mapped[int] — это аннотация типа (как в обычном dataclass), плюс
# mapped_column() — настройки самой колонки (primary_key, ForeignKey,
# nullable — по умолчанию берётся из Mapped[int] vs Mapped[int | None]).
#
# relationship() — НЕ колонка в таблице. Это Python-атрибут, который
# ORM заполняет сам: у Author будет список его Post, у Post — сам
# объект Author. back_populates связывает два relationship() друг с
# другом — меняешь один конец, синхронизируется другой.


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    posts: Mapped[List["Post"]] = relationship(back_populates="author")


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    published: Mapped[bool] = mapped_column(default=False)

    author: Mapped["Author"] = relationship(back_populates="posts")


# ════════════════════════════════════════════════════════════════════════
# 4. Base.metadata.create_all() — создание таблиц
# ════════════════════════════════════════════════════════════════════════
# Тот же самый вызов, что в Core (07_sqlalchemy_core_demo.py) — потому
# что под капотом ORM-модели ВСЁ РАВНО строят обычные Core Table-
# объекты. ORM — это слой поверх Core, не замена ему (увидишь это же
# в разделе 8 — Core-запросы работают и с ORM-моделями).

engine = create_engine(
    "postgresql+psycopg://learning:learning@localhost:5432/learning"
)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# ════════════════════════════════════════════════════════════════════════
# 5. Session — session.add()/commit(), отличие от engine.begin()
# ════════════════════════════════════════════════════════════════════════
# engine.begin() в Core выполнял SQL сразу — INSERT улетал в БД внутри
# execute(). Session работает иначе: session.add(obj) кладёт объект в
# "очередь на сохранение" в памяти, а session.commit() одним махом
# превращает всю очередь в INSERT-ы и коммитит транзакцию. До commit()
# объект существует только на стороне Python.
#
# Мнемоника: add() = git add (застейджил изменение), commit() = и
# застейджил, и сразу отправил в БД одним действием — session сама
# решает, когда именно генерировать SQL.

with Session(engine) as session:
    author = Author(name="Иван Петров")
    session.add(author)
    session.commit()

    # После commit() у author уже есть id — Session сама подставила
    # значение, которое сервер сгенерировал через SERIAL/PRIMARY KEY.
    print(author.id, author.name)
    # 1 Иван Петров

    post1 = Post(title="Введение в SQL", author_id=author.id, published=True)
    post2 = Post(title="Основы JOIN", author_id=author.id, published=False)
    session.add_all([post1, post2])
    session.commit()

# ════════════════════════════════════════════════════════════════════════
# 6. Запрос через select(Model) — результат: ОБЪЕКТЫ, не кортежи
# ════════════════════════════════════════════════════════════════════════
# select(Author) выглядит так же, как select(authors) в Core — но
# .scalars() говорит "верни мне сами объекты Author, а не Row-кортежи
# с одним элементом внутри". Без .scalars() получил бы [(<Author>,)] —
# кортеж из одного объекта на строку, а не сам объект.

with Session(engine) as session:
    query = select(Author).where(Author.name == "Иван Петров")
    result = session.execute(query).scalars().all()
    for a in result:
        print(a.id, a.name, type(a))
    # 1 Иван Петров <class '__main__.Author'>

# ════════════════════════════════════════════════════════════════════════
# 7. Доступ к relationship — author.posts без ручного JOIN
# ════════════════════════════════════════════════════════════════════════
# Вот главная выгода ORM. В Core (и в сыром SQL) для "все посты этого
# автора" нужен был явный JOIN. Здесь — просто атрибут .posts, ORM сама
# сходила в БД и подставила список Post. Это называется "ленивая
# загрузка" (lazy loading) — запрос уходит в БД в момент первого
# обращения к .posts, а не заранее.

with Session(engine) as session:
    query = select(Author).where(Author.name == "Иван Петров")
    author = session.execute(query).scalars().one()
    for post in author.posts:
        print(post.title, post.published)
    # Введение в SQL True
    # Основы JOIN False

# ════════════════════════════════════════════════════════════════════════
# 8. select(Model.col, ...).join(...) — Core-запросы всё ещё доступны
# ════════════════════════════════════════════════════════════════════════
# Для агрегатов (COUNT/SUM/GROUP BY) ORM ничего не меняет — пишешь
# ровно такой же Core-запрос, что в 07_sqlalchemy_core_demo.py, просто
# используя классы (Author.name) вместо Table-объектов (authors.c.name).
# .join() здесь тоже видит ForeignKey и сам строит ON-условие.

with Session(engine) as session:
    query = (
        select(Author.name, func.count(Post.id))
        .join(Post)
        .group_by(Author.name)
    )
    result = session.execute(query).all()
    print(result)
    # [('Иван Петров', 2)]

# ════════════════════════════════════════════════════════════════════════
# 9. Итог: Core vs ORM
# ════════════════════════════════════════════════════════════════════════
# | Core                                    | ORM                              |
# |------------------------------------------|-----------------------------------|
# | Table("authors", metadata, Column(...))  | class Author(Base): __tablename__ |
# | connection.execute(insert(authors), ...) | session.add(author); session.commit() |
# | connection.execute(select(authors))      | session.execute(select(Author)).scalars() |
# | Результат — кортежи (Row)                | Результат — объекты класса        |
# | JOIN для связанных данных — вручную      | author.posts — атрибут сам подгружает |
# | Агрегаты (GROUP BY/COUNT) — select(...)  | select(...) — тот же синтаксис    |
#
# ORM не заменяет Core — он добавляет поверх него объекты и
# relationship(), но для агрегатов и сложных запросов ты всё равно
# пишешь Core-подобный select(). Дальше в блоке — Alembic (миграции):
# как менять схему (добавить колонку, переименовать таблицу) без
# ручного DROP/CREATE, который мы использовали для перезапуска демо.
