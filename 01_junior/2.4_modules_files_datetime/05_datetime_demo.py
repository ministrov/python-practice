# -*- coding: utf-8 -*-
"""
Блок 2.4.3: Демо — дата и время
════════════════════════════════════════════════════════════════════════
Темы:
  1. date — календарная дата, без времени
  2. datetime — дата + время вместе
  3. time — время без даты (редко нужен сам по себе)
  4. timedelta — разница/интервал между датами
  5. Форматирование: strftime — дата -> строка
  6. Парсинг: strptime — строка -> дата
  7. ISO-формат: isoformat() / fromisoformat()
  8. Часовые пояса — обзорно (zoneinfo)
"""

from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

# ════════════════════════════════════════════════════════════════════════
# 1. date — только дата, без времени
# ════════════════════════════════════════════════════════════════════════

today = date.today()
print(type(today).__name__)   # date
print(today.year > 2000)      # True (сегодняшний год определённо позже)

birthday = date(2000, 5, 17)
print(birthday)                  # 2000-05-17
print(birthday.weekday())        # 2 — 0=понедельник ... 6=воскресенье
print(birthday.isoweekday())     # 3 — 1=понедельник ... 7=воскресенье


# ════════════════════════════════════════════════════════════════════════
# 2. datetime — дата + время вместе
# ════════════════════════════════════════════════════════════════════════

now = datetime.now()
print(type(now).__name__)     # datetime

meeting = datetime(2026, 8, 1, 14, 30)   # 1 августа 2026, 14:30
print(meeting)                            # 2026-08-01 14:30:00

# datetime можно собрать из отдельных date и time
d = date(2026, 12, 31)
t = time(23, 59, 59)
new_year_eve = datetime.combine(d, t)
print(new_year_eve)           # 2026-12-31 23:59:59


# ════════════════════════════════════════════════════════════════════════
# 3. time — только время (без даты)
# ════════════════════════════════════════════════════════════════════════

lunch_time = time(13, 0)
print(lunch_time)             # 13:00:00
print(lunch_time.hour, lunch_time.minute)   # 13 0


# ════════════════════════════════════════════════════════════════════════
# 4. timedelta — интервал между датами
# ════════════════════════════════════════════════════════════════════════
# Вычитание двух date/datetime даёт timedelta. timedelta можно прибавлять
# обратно к дате — получится новая дата.

gap = meeting - datetime(2026, 7, 1)
print(gap)               # 31 days, 14:30:00
print(gap.days)          # 31 — целые дни, без учёта часов

week_later = today + timedelta(days=7)
print(week_later == today + timedelta(weeks=1))   # True

deadline = date(2026, 1, 1) + timedelta(weeks=2, days=3)
print(deadline)           # 2026-01-18


# ════════════════════════════════════════════════════════════════════════
# 5. Форматирование: strftime — дата -> строка по шаблону
# ════════════════════════════════════════════════════════════════════════
# %Y — год (4 цифры), %m — месяц (2 цифры), %d — день, %H:%M — часы:мин
# %B — полное название месяца, %A — полное название дня недели

print(meeting.strftime("%d.%m.%Y"))          # 01.08.2026
print(meeting.strftime("%Y-%m-%d %H:%M"))    # 2026-08-01 14:30
print(meeting.strftime("%B %d, %Y"))         # August 01, 2026
print(meeting.strftime("%A"))                # Saturday


# ════════════════════════════════════════════════════════════════════════
# 6. Парсинг: strptime — строка -> datetime по тому же шаблону
# ════════════════════════════════════════════════════════════════════════
# Шаблон должен ТОЧНО соответствовать формату строки, иначе ValueError.

parsed = datetime.strptime("15/03/2026", "%d/%m/%Y")
print(parsed)                       # 2026-03-15 00:00:00
print(parsed.year, parsed.month, parsed.day)   # 2026 3 15

try:
    datetime.strptime("15/03/2026", "%Y-%m-%d")   # формат не совпадает
except ValueError as e:
    print(f"ValueError: {e}")


# ════════════════════════════════════════════════════════════════════════
# 7. ISO-формат: isoformat() / fromisoformat()
# ════════════════════════════════════════════════════════════════════════
# ISO 8601 ("2026-08-01T14:30:00") — стандартный однозначный формат для
# хранения дат (в JSON, БД, логах) — предпочтительнее произвольных строк.

iso_string = meeting.isoformat()
print(iso_string)                     # 2026-08-01T14:30:00

restored = datetime.fromisoformat(iso_string)
print(restored == meeting)            # True — распарсилось точно обратно


# ════════════════════════════════════════════════════════════════════════
# 8. Часовые пояса — обзорно (zoneinfo)
# ════════════════════════════════════════════════════════════════════════
# datetime без указанного часового пояса ("наивный") — просто числа, без
# привязки к месту на Земле. datetime С часовым поясом ("aware") знает,
# в какой момент по UTC он произошёл — такие можно сравнивать между собой
# для разных городов, наивные для этого не годятся.

naive = datetime(2026, 8, 1, 14, 30)
print(naive.tzinfo)   # None — наивный datetime

# На некоторых системах (в т.ч. Windows) база часовых поясов IANA не
# встроена — нужен пакет tzdata (pip install tzdata). Ловим это явно,
# чтобы демо не падало там, где его нет: сам синтаксис ниже рабочий.
try:
    aware_moscow = datetime(
        2026, 8, 1, 14, 30, tzinfo=ZoneInfo("Europe/Moscow")
    )
    print(aware_moscow.tzinfo)             # Europe/Moscow
    aware_ny = aware_moscow.astimezone(ZoneInfo("America/New_York"))
    print(aware_ny)                        # тот же момент по нью-йоркски
except ZoneInfoNotFoundError:
    print(
        "tzdata не установлена (типично для Windows без pip install "
        "tzdata) — синтаксис ZoneInfo(...) выше рабочий, просто нужна "
        "эта зависимость."
    )
