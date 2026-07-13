# -*- coding: utf-8 -*-
"""
Блок 2.4.2: Практика — работа с файлами продвинуто
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 03_files_advanced_demo.py, если застрял с форматом.
Все файлы можно писать в подпапку playground/ рядом с этим файлом —
создай её через Path.mkdir(exist_ok=True), как в демо.
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent
PLAYGROUND = BASE_DIR / "playground"

print("=" * 60)
print("ЗАДАНИЕ 1: Path — разбор пути на части")
print("=" * 60)
print("""
1.1 Создай path = Path("reports/2026/summary.txt") (путь не обязан
    существовать на диске — Path просто разбирает строку).
1.2 Напечатай path.name, path.stem, path.suffix, path.parent.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: write_text / read_text")
print("=" * 60)
print("""
2.1 Создай папку PLAYGROUND (mkdir(exist_ok=True)).
2.2 Запиши в PLAYGROUND/quote.txt любую цитату через write_text
    (encoding="utf-8").
2.3 Прочитай файл обратно через read_text и напечатай.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: iterdir и glob")
print("=" * 60)
print("""
3.1 В PLAYGROUND создай ещё 2 файла: notes.txt и data.csv (пустые
    или с любым текстом — не важно).
3.2 Через iterdir() напечатай имена ВСЕХ файлов в PLAYGROUND
    (отсортированно, sorted()).
3.3 Через glob("*.txt") напечатай имена только .txt-файлов.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: CSV — запись и чтение")
print("=" * 60)
print("""
4.1 Импортируй csv (import csv наверху файла).
4.2 Запиши в PLAYGROUND/employees.csv таблицу через csv.writer:
    заголовок ["name", "salary"], затем 3 строки с любыми данными.
4.3 Прочитай файл через csv.reader и напечатай все строки.
4.4 Прочитай ТОТ ЖЕ файл ещё раз через csv.DictReader и напечатай
    все строки как словари.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: JSON — запись и чтение файла")
print("=" * 60)
print("""
5.1 Импортируй json (import json наверху файла).
5.2 Создай словарь profile с любыми полями (например, name, age,
    hobbies — список строк).
5.3 Сохрани его в PLAYGROUND/profile.json через json.dump
    (ensure_ascii=False, indent=2).
5.4 Загрузи обратно через json.load, напечатай, и проверь через
    `==`, что загруженный словарь равен исходному.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: JSON — dumps/loads без файла")
print("=" * 60)
print("""
6.1 Преобразуй тот же словарь profile в строку через json.dumps
    (ensure_ascii=False), напечатай строку.
6.2 Преобразуй строку обратно в словарь через json.loads,
    напечатай и сравни с profile через `==`.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Бинарные файлы")
print("=" * 60)
print("""
7.1 Запиши в PLAYGROUND/data.bin любые байты, например
    b"\\x10\\x20\\x30" через write_bytes.
7.2 Прочитай обратно через read_bytes и напечатай.
7.3 Проверь через `==`, что прочитанные байты равны исходным.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Комплексное — UnicodeDecodeError")
print("=" * 60)
print("""
8.1 Запиши в PLAYGROUND/mystery.txt строку "Привет, мир" в
    кодировке "cp1251" (через .encode("cp1251") + write_bytes,
    как в демо).
8.2 Попробуй прочитать этот файл через read_text(encoding="utf-8")
    внутри try/except UnicodeDecodeError — поймай ошибку и
    напечатай понятное сообщение.
8.3 Прочитай ТОТ ЖЕ файл правильно — с encoding="cp1251" — и
    напечатай успешный результат.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("КОНЕЦ ЗАДАНИЙ, ПРОВЕРЬ ЧТО ВСЕ ЗАДАНИЯ РАБОТАЮТ!")
print("=" * 60)
