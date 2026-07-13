# -*- coding: utf-8 -*-
"""
Блок 2.4.2: Демо — работа с файлами продвинуто
════════════════════════════════════════════════════════════════════════
Темы:
  1. pathlib.Path — путь как объект, а не строка
  2. Path.write_text() / Path.read_text() — короткая запись/чтение
  3. Работа с директориями: mkdir, iterdir, glob
  4. CSV: csv.writer/reader, DictWriter/DictReader
  5. JSON: json.dump/load, dumps/loads
  6. Бинарные файлы и кодировки, UnicodeDecodeError

Базовый open()/with уже пройден в блоке 2.1 (тема 7) — здесь только
инструменты ПОВЕРХ него. Демо создаёт папку sample_data/ рядом с собой
и пишет туда файлы — это нормально, так наглядно видно реальный I/O.
"""

import csv
import json
from pathlib import Path

# ════════════════════════════════════════════════════════════════════════
# 1. pathlib.Path — путь как объект
# ════════════════════════════════════════════════════════════════════════
# Path вместо склейки строк через "+" или os.path.join. Оператор "/"
# соединяет части пути кроссплатформенно — на Windows и Linux работает
# одинаково, сам Path подставит нужный разделитель.

base_dir = Path(__file__).parent   # папка, где лежит ЭТОТ файл
data_dir = base_dir / "sample_data"

sample_file = data_dir / "note.txt"
print(sample_file.name)      # note.txt
print(sample_file.stem)      # note — имя без расширения
print(sample_file.suffix)    # .txt
print(sample_file.parent == data_dir)  # True


# ════════════════════════════════════════════════════════════════════════
# 2. Path.write_text() / Path.read_text()
# ════════════════════════════════════════════════════════════════════════
# Короче, чем open(...) as f: f.write(...) — для простых случаев без
# построчного контроля. encoding указываем так же явно, как в open().

data_dir.mkdir(exist_ok=True)   # exist_ok=True — не упадёт, если уже есть

sample_file.write_text("Привет из pathlib!\n", encoding="utf-8")
print(sample_file.exists())    # True
print(sample_file.is_file())   # True
print(sample_file.read_text(encoding="utf-8"))  # Привет из pathlib!


# ════════════════════════════════════════════════════════════════════════
# 3. Работа с директориями: iterdir, glob
# ════════════════════════════════════════════════════════════════════════

(data_dir / "second.txt").write_text("ещё файл", encoding="utf-8")
(data_dir / "placeholder.csv").write_text("", encoding="utf-8")

print("--- iterdir(): все файлы в папке ---")
for path in sorted(data_dir.iterdir()):
    print(path.name)
# note.txt, placeholder.csv, second.txt (в алфавитном порядке)

print("--- glob('*.txt'): только .txt ---")
for path in sorted(data_dir.glob("*.txt")):
    print(path.name)
# note.txt, second.txt — placeholder.csv не подошёл под маску


# ════════════════════════════════════════════════════════════════════════
# 4. CSV: csv.writer / csv.reader
# ════════════════════════════════════════════════════════════════════════
# CSV — текстовый формат таблиц: строка файла = строка таблицы, значения
# разделены запятой. Модуль csv сам разбирается с кавычками и запятыми
# внутри значений — не парси CSV вручную через split(",").

csv_path = data_dir / "report.csv"

with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerow(["Anna", 90])
    writer.writerow(["Boris", 75])

with open(csv_path, "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['name', 'score']
# ['Anna', '90']
# ['Boris', '75']

# csv.DictReader — работает со словарями, первая строка файла становится
# ключами
with open(csv_path, "r", encoding="utf-8", newline="") as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        print(row)
# {'name': 'Anna', 'score': '90'}
# {'name': 'Boris', 'score': '75'}
# Важно: значения из csv ВСЕГДА строки, даже "90" — типы приводим сами


# ════════════════════════════════════════════════════════════════════════
# 5. JSON: json.dump / json.load
# ════════════════════════════════════════════════════════════════════════
# JSON — текстовый формат для структур данных (словари, списки, числа,
# строки, bool, None). dict/list <-> JSON почти без потерь.

json_path = data_dir / "config.json"

config: dict[str, object] = {
    "debug": True,
    "retries": 3,
    "tags": ["junior", "python"],
}

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

with open(json_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded)             # {'debug': True, 'retries': 3, 'tags': [...]}
print(loaded == config)   # True — json.load вернул эквивалентный dict

# dumps/loads (с "s") — то же самое, но со строкой в памяти, без файла
text = json.dumps(config, ensure_ascii=False)
print(text)   # {"debug": true, "retries": 3, "tags": ["junior", "python"]}
print(json.loads(text) == config)  # True


# ════════════════════════════════════════════════════════════════════════
# 6. Бинарные файлы и кодировки
# ════════════════════════════════════════════════════════════════════════
# Режимы "rb"/"wb" — БЕЗ encoding, работают с bytes напрямую, а не str.
# Нужны для не-текстовых файлов (картинки, архивы) или когда важен
# контроль над самими байтами.

binary_path = data_dir / "raw.bin"
binary_path.write_bytes(b"\x00\x01\x02\xff")
print(binary_path.read_bytes())   # b'\x00\x01\x02\xff'

# encoding имеет значение и для текстовых файлов: если записали в одной
# кодировке, а читаем в другой — получим мусор или UnicodeDecodeError.
broken_path = data_dir / "broken.txt"
broken_path.write_bytes("Привет".encode("cp1251"))   # запись в cp1251

try:
    broken_path.read_text(encoding="utf-8")   # а читаем как utf-8
except UnicodeDecodeError as e:
    print(f"UnicodeDecodeError: {e}")

# Правильно: читать в ТОЙ ЖЕ кодировке, что писали
print(broken_path.read_text(encoding="cp1251"))   # Привет
