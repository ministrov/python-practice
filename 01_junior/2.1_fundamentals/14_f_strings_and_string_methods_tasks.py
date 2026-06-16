"""
ПРАКТИКА: f-строки и методы строк — 12 задач
Реши эти задачи, используя f-строки, форматирование и методы str

Запусти файл: python 14_f_strings_and_string_methods_tasks.py
"""

print("=" * 55)
print("ЗАДАЧА 1: Вставить переменные в текст")
print("=" * 55)

# Напиши функцию greet(name: str, age: int) -> str
# Возвращает строку: "Привет, {name}! Тебе {age} лет."
# Используй f-строку
#
# Пример: greet("Боб", 30) → "Привет, Боб! Тебе 30 лет."


def greet(name: str, age: int) -> str:
    return f"Привет, {name}! Тебе {age} лет."


print(greet("Алиса", 25))
print(greet("Боб", 30))


print("\n" + "=" * 55)
print("ЗАДАЧА 2: Форматирование цены")
print("=" * 55)

# Напиши функцию format_price(price: float) -> str
# Возвращает цену с двумя знаками после запятой
# Пример: format_price(19.5) → "Цена: 19.50 руб."


def format_price(price: float) -> str:
    return f"Цена: {price:.2f} руб."


print(format_price(19.5))
print(format_price(100))
print(format_price(1234.567))


print("\n" + "=" * 55)
print("ЗАДАЧА 3: Очистить строку от пробелов")
print("=" * 55)

# Напиши функцию clean(text: str) -> str
# Убирает пробелы в начале и конце
# Используй strip()
#
# Пример: clean("  hello  ") → "hello"


def clean(text: str) -> str:
    return text.strip()


print(f"'{clean('  hello  ')}'")
print(f"'{clean('world')}'")


print("\n" + "=" * 55)
print("ЗАДАЧА 4: Найти позицию подстроки")
print("=" * 55)

# Напиши функцию find_position(text: str, substring: str) -> int
# Возвращает индекс первого вхождения substring в text
# Если не найдена — возвращает -1
# Используй find()
#
# Пример: find_position("Hello World", "World") → 6


def find_position(text: str, substring: str) -> int:
    return text.find(substring)


print(find_position("Hello World", "World"))
print(find_position("Python", "xyz"))


print("\n" + "=" * 55)
print("ЗАДАЧА 5: Сосчитать количество букв")
print("=" * 55)

# Напиши функцию count_char(text: str, char: str) -> int
# Возвращает, сколько раз встречается символ char в text
# Используй count()
#
# Пример: count_char("banana", "a") → 3


def count_char(text: str, char: str) -> int:
    return text.count(char)


print(count_char("banana", "a"))
print(count_char("hello", "l"))
print(count_char("xyz", "a"))


print("\n" + "=" * 55)
print("ЗАДАЧА 6: Заменить подстроку")
print("=" * 55)

# Напиши функцию replace_word(text: str, old: str, new: str) -> str
# Заменяет все вхождения old на new
# Используй replace()
#
# Пример: replace_word("cat and cat", "cat", "dog") → "dog and dog"


def replace_word(text: str, old: str, new: str) -> str:
    return text.replace(old, new)


print(replace_word("cat and cat", "cat", "dog"))
print(replace_word("hello world", "world", "Python"))


print("\n" + "=" * 55)
print("ЗАДАЧА 7: Проверить начало и конец строки")
print("=" * 55)

# Напиши функцию validate_email(email: str) -> bool
# Возвращает True, если email начинается с буквы и кончается на ".com"
# Используй startswith(), endswith(), isalpha()
#
# Пример: validate_email("alice@example.com") → True (но нужна букава в начале)
# Примечание: это упрощённая проверка


def validate_email(email: str) -> bool:
    return bool(email) and email[0].isalpha() and email.endswith(".com")


print(validate_email("alice@example.com"))
print(validate_email("123@example.com"))
print(validate_email("bob@mail.org"))


print("\n" + "=" * 55)
print("ЗАДАЧА 8: Вырезать подстроку (срез)")
print("=" * 55)

# Напиши функцию get_middle(text: str) -> str
# Возвращает середину строки (символы со 2-го по предпоследний)
# Используй срезы [начало:конец]
#
# Пример: get_middle("hello") → "ell" (индексы 1, 2, 3)
# Пример: get_middle("ab") → "" (слишком короткая)


def get_middle(text: str) -> str:
    return text[1:-1]


print(f"'{get_middle('hello')}'")
print(f"'{get_middle('python')}'")
print(f"'{get_middle('ab')}'")


print("\n" + "=" * 55)
print("ЗАДАЧА 9: Разбить и собрать строку")
print("=" * 55)

# Напиши функцию reverse_words(text: str) -> str
# Разбивает текст на слова, переворачивает их порядок и собирает обратно
# Используй split() и join()
#
# Пример: reverse_words("Hello World Python") → "Python World Hello"


def reverse_words(text: str) -> str:
    result: list[str] = []
    splitted_text = text.split()

    for word in reversed(splitted_text):
        result.append(word)

    return " ".join(result)


print(reverse_words("Hello World Python"))
print(reverse_words("one two three"))


print("\n" + "=" * 55)
print("ЗАДАЧА 10: Преобразовать регистр и удалить пробелы")
print("=" * 55)

# Напиши функцию normalize(text: str) -> str
# 1. Убирает пробелы в начале/конце (strip)
# 2. Переводит в нижний регистр (lower)
# 3. Заменяет пробелы на подчеркивания (replace)
#
# Пример: normalize("  Hello World  ") → "hello_world"


def normalize(text: str) -> str:
    return text.strip().lower().replace(" ", "_")


print(normalize("  Hello World  "))
print(normalize("Python IS Cool"))


print("\n" + "=" * 55)
print("ЗАДАЧА 11: Парсить и форматировать данные")
print("=" * 55)

# Напиши функцию parse_csv_line(line: str) -> str
# Получает строку вида "name,age,city"
# Возвращает отформатированную: "name: ???, age: ???, city: ???"
# Используй split() и f-строку
#
# Пример: parse_csv_line("Alice,25,Moscow") → "name: Alice, age: 25, city: Moscow"


def parse_csv_line(line: str) -> str:
    return f"name: {line.split(',')[0]}, age: {line.split(',')[1]}, city: {line.split(',')[2]}"


print(parse_csv_line("Alice,25,Moscow"))
print(parse_csv_line("Bob,30,London"))


print("\n" + "=" * 55)
print("ЗАДАЧА 12: Подсчитать статистику строки")
print("=" * 55)

# Напиши функцию analyze(text: str) -> str
# Возвращает статистику в формате:
# "Текст: '...', Длина: N, Слов: N, Букв: N (только буквы)"
# Используй len(), split(), count(), методы проверки типа (isalpha)
#
# Пример: analyze("Hello World") → "Текст: 'Hello World', Длина: 11, Слов: 2, Букв: 10"


def analyze(text: str) -> str:
    letters = sum(1 for c in text if c.isalpha())
    return f"Текст: '{text}', Длина: {len(text)}, Слов: {len(text.split())}, Букв: {letters}"


print(analyze("Hello World"))
print(analyze("Python 123 Cool"))
