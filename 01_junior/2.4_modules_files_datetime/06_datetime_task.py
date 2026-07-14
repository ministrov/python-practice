# -*- coding: utf-8 -*-
"""
Блок 2.4.3: Практика — дата и время
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 05_datetime_demo.py, если застрял с форматом.
"""
import datetime

print("=" * 60)
print("ЗАДАНИЕ 1: date — базовые атрибуты")
print("=" * 60)
print("""
1.1 Импортируй нужное из datetime (date, datetime, time, timedelta
    понадобятся по ходу заданий — добавляй по мере необходимости).
1.2 Создай birthday = date(год, месяц, день) с любой датой в прошлом.
1.3 Напечатай год, месяц, день по отдельности (birthday.year и т.д.).
1.4 Напечатай день недели через weekday() и через isoweekday() —
    сравни разницу в комментарии (что означает 0 в каждом из них).
""")

# ТВОЙ КОД ЗДЕСЬ:
birthday = datetime.date(1984, 12, 25)
print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.weekday())
print(birthday.isoweekday())
# weekday() считает от 0 (пн), isoweekday() — от 1 (пн);
# 0 в isoweekday() не встречается никогда.

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: datetime.combine")
print("=" * 60)
print("""
2.1 Создай отдельно d = date(...) и t = time(...) с любыми
    значениями.
2.2 Собери из них datetime через datetime.combine(d, t).
2.3 Напечатай результат.
""")

# ТВОЙ КОД ЗДЕСЬ:
d = datetime.date(2020, 2, 2)
t = datetime.time(19, 2, 2)
dt = datetime.datetime.combine(d, t)
print(dt)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: timedelta — разница и прибавление")
print("=" * 60)
print("""
3.1 Создай две даты: start = date(...) и end = date(...), где
    end позже start минимум на месяц.
3.2 Вычисли gap = end - start, напечатай gap и gap.days.
3.3 Прибавь к start timedelta(days=100) и напечатай результат.
""")

# ТВОЙ КОД ЗДЕСЬ:
start = datetime.date(2020, 2, 4)
end = datetime.date(2020, 3, 5)
gap = end - start
print(gap)
print(gap.days)
print(start + datetime.timedelta(days=100))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: strftime — форматирование")
print("=" * 60)
print("""
4.1 Возьми datetime.now() и напечатай его в трёх форматах:
    - "ДД.ММ.ГГГГ" (например, 14.07.2026)
    - "ГГГГ-ММ-ДД ЧЧ:ММ"
    - полное название дня недели (%A) и месяца (%B) вместе,
      например "Tuesday, July"
""")

# ТВОЙ КОД ЗДЕСЬ:
now = datetime.datetime.now()
print(now.strftime("%d.%m.%Y"))
print(now.strftime("%Y-%m-%d %H:%M"))
print(now.strftime("%A, %B"))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: strptime — парсинг строк")
print("=" * 60)
print("""
5.1 Есть строка "2026-11-05 09:15" — распарси её в datetime через
    strptime с подходящим форматом, напечатай результат и год/месяц.
5.2 Попробуй распарсить ЭТУ ЖЕ строку заведомо неправильным форматом
    внутри try/except ValueError — поймай ошибку, напечатай текст.
""")

# ТВОЙ КОД ЗДЕСЬ:

s = "2026-11-05 09:15"

# 5.1
dt = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M")
print(dt)
print(dt.year, dt.month)

# 5.2
try:
    datetime.datetime.strptime(s, "%d/%m/%Y")
except ValueError as e:
    print("Ошибка:", e)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: ISO-формат")
print("=" * 60)
print("""
6.1 Возьми любой datetime, преобразуй в ISO-строку через
    isoformat().
6.2 Преобразуй строку обратно в datetime через fromisoformat().
6.3 Проверь через `==`, что результат совпадает с исходным datetime.
""")

# ТВОЙ КОД ЗДЕСЬ:
# 6.1
dt = datetime.datetime(2026, 11, 5, 9, 15, 30)
iso = dt.isoformat()
print(iso)

# 6.2
dt2 = datetime.datetime.fromisoformat(iso)
print(dt2)

# 6.3
print(dt == dt2)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Возраст в днях")
print("=" * 60)
print("""
7.1 Напиши функцию days_since(d: date) -> int, которая возвращает
    сколько дней прошло от даты d до date.today() (используй
    timedelta, который получается при вычитании дат).
7.2 Проверь на дате своего дня рождения (или любой другой дате
    в прошлом) — результат должен быть положительным числом.
""")

# ТВОЙ КОД ЗДЕСЬ:


def days_since(d: datetime.date) -> int:
    return (datetime.date.today() - d).days


print(days_since(datetime.date(2000, 1, 1)))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Комплексное — дедлайн")
print("=" * 60)
print("""
8.1 Напиши функцию format_deadline(start: date, days_left: int) -> str,
    которая:
    - вычисляет дедлайн = start + timedelta(days=days_left)
    - возвращает строку вида
      f"Дедлайн: {дедлайн в формате ДД.ММ.ГГГГ} ({день недели, %A})"
8.2 Вызови format_deadline(date.today(), 30) и напечатай результат.
""")

# ТВОЙ КОД ЗДЕСЬ:


def format_deadline(start: datetime.date, days_left: int) -> str:
    deadline = start + datetime.timedelta(days=days_left)
    return f"Дедлайн: {deadline.strftime('%d.%m.%Y')} ({deadline.strftime('%A')})"


print(format_deadline(datetime.date.today(), 30))

print("\n" + "=" * 60)
print("КОНЕЦ ЗАДАНИЙ, ПРОВЕРЬ ЧТО ВСЕ ЗАДАНИЯ РАБОТАЮТ!")
print("=" * 60)
