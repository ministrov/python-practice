# -*- coding: utf-8 -*-
"""
Блок 2.7.2: Практика — raise from, цепочки исключений, ExceptionGroup
════════════════════════════════════════════════════════════════════════
7 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 03_raise_from_demo.py если застрял.
"""

import json


print("=" * 60)
print("ЗАДАНИЕ 1: Неявная цепочка")
print("=" * 60)
print("""
1.1 Напиши функцию load_config(raw: str) -> dict[str, str], которая
    вызывает json.loads(raw) (импортируй json) и, если json.loads
    поднимает json.JSONDecodeError, ловит его и поднимает ВНУТРИ
    except СВОЁ исключение ConfigError("невалидный конфиг") БЕЗ
    ключевого слова from (намеренно — демонстрация неявной цепочки).
1.2 Класс ConfigError(Exception) объяви сам, ДО функции.
1.3 Вызови load_config("не json") в try/except ConfigError as e,
    поймай, выведи str(e) и e.__context__.
""")

# ТВОЙ КОД ЗДЕСЬ:


class ConfigError(Exception):
    """Ошибка уровня приложения — понятна вызывающему коду."""


def load_config(raw: str) -> dict[str, str]:
    try:
        config = json.loads(raw)
    except json.JSONDecodeError:
        raise ConfigError("невалидный конфиг")  # noqa: B904 — намеренно, демонстрация неявной цепочки

    return config


try:
    load_config("не json")
except ConfigError as e:
    print(str(e))
    print(f"__context__: {e.__context__!r}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Явная цепочка (from e)")
print("=" * 60)
print("""
2.1 Напиши divide_safe(a: float, b: float) -> float, которая делит
    a на b и, если ловит ZeroDivisionError, поднимает СВОЁ исключение
    CalculationError("деление на ноль") ЯВНО через from e.
2.2 Класс CalculationError(Exception) объяви сам.
2.3 Вызови divide_safe(10, 0) в try/except, поймай CalculationError,
    выведи str(e), e.__cause__ и e.__context__ (оба должны быть
    заполнены одним и тем же ZeroDivisionError).
""")

# ТВОЙ КОД ЗДЕСЬ:


class CalculationError(Exception):
    pass


def divide_safe(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError as e:
        raise CalculationError("деление на ноль") from e


try:
    divide_safe(10, 0)
except CalculationError as e:
    print(str(e))
    print(f"__cause__: {e.__cause__!r}")
    print(f"__context__: {e.__context__!r}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: Подавление цепочки (from None)")
print("=" * 60)
print("""
3.1 Напиши get_env_int(raw: str) -> int, которая вызывает int(raw)
    и, если ловит ValueError, поднимает СВОЁ исключение
    EnvVarError("переменная окружения должна быть числом") ЧЕРЕЗ
    from None (оригинальная ошибка — деталь реализации).
3.2 Класс EnvVarError(Exception) объяви сам.
3.3 Вызови get_env_int("not_a_number"), поймай EnvVarError, выведи
    e.__cause__ (должен быть None) и e.__suppress_context__ (должен
    быть True).
""")

# ТВОЙ КОД ЗДЕСЬ:


class EnvVarError(Exception):
    pass


def get_env_int(raw: str) -> int:
    try:
        return int(raw)
    except ValueError:
        raise EnvVarError("переменная окружения должна быть числом") from None


try:
    get_env_int("сорок")
except EnvVarError as e:
    print(f"\n__cause__: {e.__cause__!r}")
    print(f"__context__: {e.__context__!r}")
    print(f"__suppress_context__: {e.__suppress_context__!r}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: Сравнение всех трёх на одном примере")
print("=" * 60)
print("""
4.1 У тебя уже есть 3 варианта одной и той же идеи (задания 1-3).
    В комментарии ниже (НЕ код) напиши своими словами: чем ситуация,
    когда стоит использовать `from e`, отличается от ситуации, когда
    стоит использовать `from None`? Приведи свой пример (не из демо)
    на каждый случай.
""")

# ТВОЙ ОТВЕТ ЗДЕСЬ (в комментарии):
# `from e` используем, когда причина исключения — важная диагностическая
# информация, полезная для отладки или логирования. Мы просто оборачиваем
# низкоуровневую ошибку в более понятную для вызывающего кода, но не хотим
# терять исходный трейсбек — например, при работе с БД или внешним API,
# где важно видеть, что именно пошло не так "под капотом".
#
# Пример: функция fetch_user(user_id) делает запрос к БД через ORM.
# Если ORM поднимает ConnectionError, мы оборачиваем его в своё
# RepositoryError("не удалось получить пользователя") from e —
# в логах увидим и наше сообщение, и оригинальный ConnectionError
# с деталями (какой хост, таймаут и т.д.) — это нужно для дебага.

# `from None` используем, когда причина исключения — деталь реализации,
# которая ничего не даёт вызывающему коду и только засоряет трейсбек.
# Обычно это ситуации, где мы валидируем пользовательский ввод и хотим
# показать чистую, понятную ошибку без "мусора" из внутренностей.
#
# Пример: функция parse_phone(raw: str) пытается распарсить номер
# телефона через регулярку/int(). Если это падает с ValueError, нам
# не важно видеть внутренний ValueError в трейсбеке — важно только
# сообщение "невалидный формат номера телефона". Поэтому поднимаем
# PhoneFormatError(...) from None — чище для логов и конечного
# пользователя API (например, в ответе 400 Bad Request).

# Короче: from e — когда причина полезна (баги, инфраструктура, дебаг).
# from None — когда причина не нужна и только шумит (валидация ввода).

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: ExceptionGroup — собери все ошибки сразу")
print("=" * 60)
print("""
5.1 Напиши check_password(password: str) -> None, которая проверяет
    ТРИ условия и для каждого нарушенного добавляет ValueError в
    список errors (НЕ поднимает сразу, копит все):
      - длина >= 8 символов, иначе ValueError("слишком короткий")
      - есть хотя бы одна цифра, иначе ValueError("нет цифры")
      - есть хотя бы одна заглавная буква, иначе
        ValueError("нет заглавной буквы")
5.2 Если errors не пуст — подними
    ExceptionGroup("ошибки пароля", errors)
5.3 Проверь check_password("abc") — должны найтись ВСЕ 3 ошибки
    сразу (не только первая).
""")

# ТВОЙ КОД ЗДЕСЬ:


def check_password(password: str) -> None:
    """Собирает ВСЕ ошибки валидации сразу, а не только первую."""
    errors: list[Exception] = []

    if len(password) < 8:
        errors.append(ValueError("слишком короткий"))

    if not any(ch.isdigit() for ch in password):
        errors.append(ValueError("нет цифры"))

    if not any(ch.isupper() for ch in password):
        errors.append(ValueError("нет заглавной буквы"))

    if errors:
        raise ExceptionGroup("ошибки пароля", errors)


try:
    check_password("abc")
except* ValueError as eg:
    for err in eg.exceptions:
        print(f"- {err}")


print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: except* — разбор группы по типам")
print("=" * 60)
print("""
6.1 Напиши run_checks() -> None, которая поднимает
    ExceptionGroup("проверки", [ValueError("v1"), TypeError("t1"),
    ValueError("v2")]) (три ошибки двух разных типов в одной группе).
6.2 Вызови run_checks() в try, с ДВУМЯ блоками except* подряд:
    except* ValueError as eg — вывести список сообщений всех
    ValueError из группы; except* TypeError as eg — вывести список
    сообщений всех TypeError из группы.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Комплексное — цепочка + ExceptionGroup вместе")
print("=" * 60)
print("""
7.1 Напиши process_records(records: list[str]) -> None, которая для
    КАЖДОЙ строки в records пытается int(record); если строка не
    парсится — ловит ValueError и оборачивает в СВОЁ RecordError
    (объяви класс сам) ЯВНО через `from e`, добавляя каждую такую
    RecordError в список errors (не прерывая цикл на первой ошибке).
7.2 После цикла: если errors не пуст — подними
    ExceptionGroup("ошибки записей", errors).
7.3 Вызови process_records(["1", "два", "3", "четыре"]) в try/except*
    RecordError as eg, выведи для каждой ошибки в группе её
    str(e) И e.__cause__ (должен быть исходный ValueError у каждой).
""")

# ТВОЙ КОД ЗДЕСЬ:
