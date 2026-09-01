# -*- coding: utf-8 -*-
"""
Блок 2.8, тема 5 (последняя): Alembic — миграции схемы БД
════════════════════════════════════════════════════════════════════════
Тема ОЗНАКОМИТЕЛЬНАЯ — только это демо, без _task.py и коммитов по
заданиям (та же трактовка, что для mypy/ruff/venv в блоке 2.6: это
инструмент вокруг SQLAlchemy, а не новый язык/API для практики).

Всё ниже выполнено по-настоящему (реальный `pip install alembic`,
реальный контейнер pg-learning, реальные команды alembic) — вывод в
комментариях скопирован из терминала как есть, не выдуман. Чтобы не
трогать таблицы authors/posts/customers/orders из прошлых тем, миграции
применялись к отдельной базе `alembic_learning` в том же контейнере
pg-learning (host=localhost, port=5432, user=learning, password=learning).

Модель — тот же Author/Post, что в 09_sqlalchemy_orm_demo.py.

Темы:
  0. Проблема: почему create_all() — не решение для реального проекта
  1. alembic init — структура проекта
  2. env.py: target_metadata = Base.metadata — источник для autogenerate
  3. alembic revision --autogenerate — первая миграция (создание таблиц)
  4. alembic upgrade head — применение, alembic_version
  5. Меняем модель, генерируем вторую миграцию
  6. Грабли: NOT NULL на непустой таблице — реальный traceback
  7. Исправление: server_default при add_column
  8. downgrade / history / current — параллель с git
  9. Итог: что autogenerate видит, а что нет
"""

# ════════════════════════════════════════════════════════════════════════
# 0. Проблема: почему create_all() — не решение для реального проекта
# ════════════════════════════════════════════════════════════════════════
# В 09_sqlalchemy_orm_demo.py каждый запуск делал:
#
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)
#
# drop_all() удаляет ВСЕ таблицы, create_all() создаёт их заново с нуля.
# Это нормально для учебной базы — данные всё равно тестовые.
#
# В реальном проекте так нельзя: drop_all() уничтожит данные пользователей.
# А create_all() САМ ПО СЕБЕ (без drop_all) тоже не помогает — он создаёт
# только те таблицы, которых ЕЩЁ НЕТ. Если ты добавил в модель Post новое
# поле `views`, create_all() эту колонку в уже существующую таблицу НЕ
# добавит — он её просто не трогает (таблица posts уже есть).
#
# Значит нужен механизм: "у меня была схема A, я хочу дойти до схемы B,
# не потеряв данные" — это и есть миграция. Alembic хранит миграции как
# последовательность файлов (как коммиты в git), каждый — маленький,
# обратимый шаг схемы.


# ════════════════════════════════════════════════════════════════════════
# 1. alembic init — структура проекта
# ════════════════════════════════════════════════════════════════════════
# pip install alembic
# alembic init migrations
#
# Реальный вывод:
#
#   Creating directory .../migrations ...  done
#   Creating directory .../migrations/versions ...  done
#   Generating .../alembic.ini ...  done
#   Generating .../migrations/env.py ...  done
#   Generating .../migrations/README ...  done
#   Generating .../migrations/script.py.mako ...  done
#
# Итоговая структура:
#
#   alembic.ini              — конфиг: путь к БД, логирование
#   migrations/
#       env.py                — код, который запускается при КАЖДОЙ
#                                команде alembic (подключение к БД,
#                                откуда брать target_metadata)
#       script.py.mako        — шаблон для новых файлов миграций
#       versions/              — сюда попадают сгенерированные миграции
#
# Параллель с git: alembic.ini ~ .git/config, versions/ ~ история
# коммитов, каждый файл миграции ~ один коммит с diff схемы.


# ════════════════════════════════════════════════════════════════════════
# 2. env.py: target_metadata = Base.metadata
# ════════════════════════════════════════════════════════════════════════
# По умолчанию в сгенерированном env.py:
#
#     target_metadata = None
#
# None означает "autogenerate ничего не сравнивает, миграции пиши руками
# с нуля". Чтобы alembic мог САМ увидеть разницу между текущей БД и
# моделями — нужно указать те же классы Base, что в SQLAlchemy-моделях:
#
#     from models import Base
#     target_metadata = Base.metadata
#
# Также в alembic.ini указывается строка подключения:
#
#     sqlalchemy.url = postgresql+psycopg://learning:learning@localhost:5432/alembic_learning
#
# С этого момента alembic знает ДВЕ вещи: какая схема есть в БД сейчас
# (через alembic_version, см. раздел 4) и какая схема ОПИСАНА в моделях
# (через target_metadata) — и может сравнивать их.


# ════════════════════════════════════════════════════════════════════════
# 3. alembic revision --autogenerate — первая миграция
# ════════════════════════════════════════════════════════════════════════
# Модель на этом шаге — Author/Post, как в 09_sqlalchemy_orm_demo.py,
# но в БД alembic_learning таблиц ещё нет вообще (свежая база).
#
# alembic revision --autogenerate -m "create authors and posts"
#
# Реальный вывод:
#
#   INFO  [alembic.autogenerate.compare.tables] Detected added table 'authors'
#   INFO  [alembic.autogenerate.compare.tables] Detected added table 'posts'
#   Generating .../versions/adce1a3634e2_create_authors_and_posts.py ...  done
#
# Alembic сравнил "в БД нет таблиц" с "в моделях есть Author и Post" и
# сгенерировал файл. Содержимое (без изменений, как сгенерировано):
#
#   def upgrade() -> None:
#       op.create_table('authors',
#       sa.Column('id', sa.Integer(), nullable=False),
#       sa.Column('name', sa.String(), nullable=False),
#       sa.PrimaryKeyConstraint('id')
#       )
#       op.create_table('posts',
#       sa.Column('id', sa.Integer(), nullable=False),
#       sa.Column('title', sa.String(), nullable=False),
#       sa.Column('author_id', sa.Integer(), nullable=False),
#       sa.Column('published', sa.Boolean(), nullable=False),
#       sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
#       sa.PrimaryKeyConstraint('id')
#       )
#
#   def downgrade() -> None:
#       op.drop_table('posts')
#       op.drop_table('authors')
#
# upgrade() — как дойти ДО этой схемы, downgrade() — как от неё
# ОТКАТИТЬСЯ. Alembic пишет оба сразу, по объявленной модели.


# ════════════════════════════════════════════════════════════════════════
# 4. alembic upgrade head — применение, alembic_version
# ════════════════════════════════════════════════════════════════════════
# alembic upgrade head
#
# Реальный вывод:
#
#   INFO  [alembic.runtime.migration] Running upgrade  -> adce1a3634e2,
#         create authors and posts
#
# "head" значит "последняя известная миграция" (опять параллель с git:
# как `git checkout main` — дойти до последнего коммита в цепочке).
#
# Проверка через psql (\dt):
#
#                List of relations
#    Schema |      Name       | Type  |  Owner
#   --------+-----------------+-------+----------
#    public | alembic_version | table | learning
#    public | authors         | table | learning
#    public | posts           | table | learning
#
# alembic_version — служебная таблица САМОГО alembic (не из моделей):
# в ней ровно одна строка с id текущей миграции. Именно по ней alembic
# в следующий раз понимает "на какой версии схемы сейчас стоит БД".


# ════════════════════════════════════════════════════════════════════════
# 5. Меняем модель, генерируем вторую миграцию
# ════════════════════════════════════════════════════════════════════════
# Добавили в класс Post новое поле:
#
#     views: Mapped[int] = mapped_column(default=0)
#
# alembic revision --autogenerate -m "add views to posts"
#
# Реальный вывод:
#
#   INFO  [alembic.autogenerate.compare.tables] Detected added column
#         'posts.views'
#   Generating .../versions/a2f63ff792b7_add_views_to_posts.py ...  done
#
# Сгенерированный upgrade() (КАК СГЕНЕРИРОВАНО, до правки):
#
#   def upgrade() -> None:
#       op.add_column('posts', sa.Column('views', sa.Integer(), nullable=False))
#
#   def downgrade() -> None:
#       op.drop_column('posts', 'views')


# ════════════════════════════════════════════════════════════════════════
# 6. Грабли: NOT NULL на непустой таблице — реальный traceback
# ════════════════════════════════════════════════════════════════════════
# В таблице posts уже есть одна строка (вставил вручную перед этим шагом,
# чтобы показать реальную ситуацию — "добавляем поле в БД, где уже есть
# данные", а не в пустую тестовую таблицу).
#
# alembic upgrade head — со сгенерированным (не правленным) upgrade()
# из раздела 5:
#
#   sqlalchemy.exc.IntegrityError: (psycopg.errors.NotNullViolation)
#   column "views" of relation "posts" contains null values
#   [SQL: ALTER TABLE posts ADD COLUMN views INTEGER NOT NULL]
#
# Почему: `views: Mapped[int] = mapped_column(default=0)` — этот
# default=0 работает ТОЛЬКО на стороне Python/ORM, когда ты создаёшь
# НОВЫЙ объект Post(...) через Session. Он ничего не знает про уже
# существующие строки в БД. ALTER TABLE ADD COLUMN ... NOT NULL требует
# значение для КАЖДОЙ существующей строки прямо сейчас, на уровне БД —
# а взять его неоткуда, раз в модели дефолт не дошёл до SQL.
#
# Это ровно то, зачем нужен autogenerate ИМЕННО как черновик, а не
# готовый к продакшену файл: он честно описывает "какая разница между
# схемами", но не знает про твои существующие данные.


# ════════════════════════════════════════════════════════════════════════
# 7. Исправление: server_default при add_column
# ════════════════════════════════════════════════════════════════════════
# Правка миграции руками (типовой паттерн для "новая NOT NULL колонка
# в непустую таблицу"):
#
#   def upgrade() -> None:
#       op.add_column(
#           'posts',
#           sa.Column('views', sa.Integer(), nullable=False, server_default='0'),
#       )
#       op.alter_column('posts', 'views', server_default=None)
#
# Два шага, не один:
#   1. add_column с server_default='0' — теперь ALTER TABLE знает, чем
#      заполнить существующие строки, и колонка создаётся успешно.
#   2. alter_column(..., server_default=None) сразу после — снимает
#      дефолт на уровне БД. Он больше не нужен: для новых строк дефолт
#      и так даёт Python-модель (default=0 в mapped_column), а
#      оставленный "навсегда" server_default в схеме — источник
#      путаницы (два места с одним и тем же значением по умолчанию,
#      которые могут разойтись).
#
# alembic upgrade head — повторно, с исправленным файлом:
#
#   INFO  [alembic.runtime.migration] Running upgrade adce1a3634e2 ->
#         a2f63ff792b7, add views to posts
#
# Проверка (\d posts + SELECT * FROM posts):
#
#    Column   |       Type        | Nullable |  Default
#   -----------+-------------------+----------+-----------
#    views     | integer           | not null |   (пусто — server_default снят)
#
#    id |   title   | author_id | published | views
#   ----+-----------+-----------+-----------+-------
#     1 | Test Post |         1 | f         |     0
#
# Старая строка получила views=0 (из временного server_default на
# момент ALTER TABLE), новый server_default в схеме не остался.


# ════════════════════════════════════════════════════════════════════════
# 8. downgrade / history / current — параллель с git
# ════════════════════════════════════════════════════════════════════════
# alembic downgrade -1   — откатить на одну миграцию назад
#   Running downgrade a2f63ff792b7 -> adce1a3634e2, add views to posts
#
# alembic history         — вся цепочка миграций (~ git log)
#   adce1a3634e2 -> a2f63ff792b7 (head), add views to posts
#   <base> -> adce1a3634e2, create authors and posts
#
# alembic current          — на какой версии стоит БД ПРЯМО СЕЙЧАС
#   adce1a3634e2
#
# Параллель с git, если проводить дальше:
#   revision id       ~ хэш коммита
#   down_revision     ~ ссылка на родительский коммит
#   alembic history   ~ git log
#   alembic current   ~ git rev-parse HEAD
#   upgrade / downgrade ~ checkout вперёд/назад по цепочке коммитов
#
# Ключевое отличие от git: alembic не просто "переключает файлы", а
# РЕАЛЬНО выполняет SQL (upgrade()/downgrade()) над живой БД — откат
# исполняет код, а не просто меняет указатель.


# ════════════════════════════════════════════════════════════════════════
# 9. Итог: что autogenerate видит, а что нет
# ════════════════════════════════════════════════════════════════════════
# ВИДИТ хорошо:
#   - новую таблицу / удалённую таблицу
#   - новую колонку / удалённую колонку
#   - смену типа колонки, nullable, foreign key
#
# НЕ видит (или видит неправильно) — нужно ПРАВИТЬ сгенерированный файл
# руками, как в разделе 7:
#   - переименование колонки/таблицы — autogenerate это увидит как
#     "удалили одну колонку + добавили другую" (потеряешь данные, если
#     применить как есть — надо вручную заменить на op.alter_column
#     с новым именем)
#   - NOT NULL колонка в непустую таблицу — нужен server_default
#     (раздел 6-7)
#   - сложные преобразования данных при миграции (например, разбить
#     одно поле full_name на first_name/last_name) — autogenerate
#     вообще не умеет писать такой код, это чистый Python в
#     upgrade()/downgrade(), который пишешь сам
#
# Практическое правило: autogenerate — это ЧЕРНОВИК, не готовый
# результат. Каждую сгенерированную миграцию нужно открыть и прочитать
# перед upgrade — как diff перед коммитом.
