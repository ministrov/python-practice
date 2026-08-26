# SQLAlchemy: выжимка Core + ORM

## 1. Общая архитектура

SQLAlchemy состоит из двух слоёв:

- **Core** — низкоуровневый: таблицы, столбцы, SQL-выражения как Python-объекты.
- **ORM** — надстройка над Core: классы Python мапятся на таблицы, объекты — на строки.

**Мнемоника:** Core — это кирпичи, ORM — дом из кирпичей.

---

## 2. Core: базовые объекты (кратко)

| Объект | Назначение |
|---|---|
| `Engine` | настройки подключения + пул соединений |
| `Connection` | реальное соединение, через которое идут запросы |
| `MetaData` | реестр всех таблиц схемы |
| `Table` / `Column` | описание таблицы и её столбцов |
| `select/insert/update/delete()` | конструкторы SQL-запросов |
| `text()` | сырой SQL, обёрнутый в SQLAlchemy |
| `Result` | объект с результатами запроса |
| `Transaction` | commit / rollback группы операций |

Цепочка: **Engine → Connection → MetaData → Table → Column → Expression → Result**

---

## 3. ORM: ключевые понятия

### 3.1 Declarative Base
Базовый класс, от которого наследуются все модели:
```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

### 3.2 Модель (mapped class)
Класс Python = таблица в БД:
```python
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str | None]
```

**Мнемоника:** `Mapped[тип]` — это «ярлык» атрибута, `mapped_column()` — его паспорт с деталями (constraints, значения по умолчанию).

### 3.3 Session — «прораб на стройке»
Главный рабочий объект ORM. Через неё идут все операции с объектами:
```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    session.add(user)
    session.commit()
```

- `session.add(obj)` — добавить объект (будущий INSERT)
- `session.query()` / `select()` + `session.execute()` — прочитать
- `session.commit()` — зафиксировать изменения
- `session.rollback()` — откатить
- `session.delete(obj)` — удалить

### 3.4 Identity Map — «список пропусков на входе»
Session хранит по одному объекту на каждую строку (по PK), избегая дублей в памяти в рамках одной сессии.

### 3.5 Unit of Work — «список покупок перед кассой»
Session накапливает все изменения (add/update/delete) и применяет их одним пакетом при `commit()`, а не сразу.

### 3.6 relationship() — «мостик между таблицами»
Связывает модели друг с другом на уровне Python-объектов (в отличие от `ForeignKey`, который связывает на уровне столбцов):
```python
class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship(back_populates="posts")

class User(Base):
    ...
    posts: Mapped[list["Post"]] = relationship(back_populates="author")
```

- `ForeignKey` — физическая связь в БД (столбец → столбец)
- `relationship()` — удобный доступ в Python (`user.posts`, `post.author`)
- `back_populates` — говорит SQLAlchemy, что две стороны связи синхронизированы

### 3.7 Стратегии загрузки связей (lazy loading)

| Стратегия | Когда грузит связанные данные |
|---|---|
| `lazy="select"` (по умолчанию) | отдельным запросом при первом обращении |
| `joinedload()` | сразу через JOIN в основном запросе |
| `selectinload()` | отдельным `SELECT ... IN (...)` — хорошо для списков |
| `subqueryload()` | через подзапрос |

**Мнемоника:** lazy = «лениво, потом»; joined/selectin = «сразу, заранее».

Проблема **N+1 запросов** — классическая ловушка, когда lazy loading вызывает по одному запросу на каждый объект в цикле. Лечится через `selectinload`/`joinedload`.

### 3.8 Session lifecycle states
Объект в ORM может быть в одном из состояний:
- **transient** — создан, но не в сессии
- **pending** — добавлен в сессию (`add()`), но ещё не в БД
- **persistent** — сохранён и синхронизирован с БД
- **detached** — был в сессии, но сессия закрыта/объект убран

---

## 4. Core vs ORM: когда что использовать

| Core | ORM |
|---|---|
| Массовые операции, аналитика, отчёты | Бизнес-логика с объектами |
| Полный контроль над SQL | Быстрая разработка через классы |
| Меньше магии — прозрачнее | Связи, каскады, identity map |

Можно использовать оба слоя одновременно: ORM под капотом сам построен поверх Core.

---

## 5. Практика с PostgreSQL

- Диалект: `postgresql+psycopg://user:pass@host:port/dbname` (psycopg 3, не `psycopg2` — так же, как в этом проекте)
- Типы PostgreSQL-специфичные: `JSONB`, `ARRAY`, `UUID` — импортируются из `sqlalchemy.dialects.postgresql`
- `Session`/`Engine` под капотом сами используют пул соединений и курсор psycopg — вручную его трогать не нужно, ORM/Core берут это на себя

---

### Общая мнемоника всей темы

**Engine (завод) → Session (прораб) → Model (чертёж класса) → relationship (мостик) → commit (сдача объекта)**
