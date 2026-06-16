"""
ДЕМО: f-строки и методы строк
Python 3.6+

Что это:
- f-строки (formatted string literals) — способ вставлять переменные в строки
- Методы str — встроенные функции для работы со строками

f-строки: f"текст {переменная} ещё текст"
Методы: "строка".upper(), "строка".lower(), и т.д.

Запусти файл: python 13_f_strings_and_string_methods_demo.py
"""

print("=" * 55)
print("1) БАЗА: f-строки")
print("=" * 55)

name = "Алиса"
age = 25

# Обычная конкатенация (старый способ)
result = "Меня зовут " + name + ", мне " + str(age) + " лет"
print(result)

# f-строка (новый способ)
result = f"Меня зовут {name}, мне {age} лет"
print(result)
print(type(result))

# Без f: строка не интерпретирует {}
print("Без f: это просто текст {name} и {age}")


print("\n" + "=" * 55)
print("2) ВЫРАЖЕНИЯ В f-строках")
print("=" * 55)

x = 10
y = 3

# Вычисления внутри {}
print(f"10 + 3 = {x + y}")
print(f"10 * 3 = {x * y}")
print(f"10 / 3 = {x / y}")

# Вызов функций внутри {}
text = "hello"
print(f"Прописные: {text.upper()}")
print(f"Длина: {len(text)}")

# Условия (тернарный оператор)
age = 25
status = f"Статус: {'взрослый' if age >= 18 else 'несовершеннолетний'}"
print(status)


print("\n" + "=" * 55)
print("3) ФОРМАТИРОВАНИЕ: ширина и выравнивание")
print("=" * 55)

name = "Боб"
price = 19.99

# Ширина поля: {переменная:ширина}
print(f"Имя: {name:10}")        # 10 символов, левое выравнивание
print(f"Имя: {name:>10}")       # 10 символов, правое выравнивание
print(f"Имя: {name:^10}")       # 10 символов, центрирование

# Заполнение символом: {переменная:символ>ширина}
print(f"Число: {123:0>5}")      # 00123 (заполнить нулями)
print(f"Число: {123:->5}")      # --123 (заполнить дефисами)


print("\n" + "=" * 55)
print("4) ФОРМАТИРОВАНИЕ: числа и десятичные")
print("=" * 55)

pi = 3.14159265

# Количество знаков после запятой: {число:.Nf}
print(f"pi = {pi:.2f}")         # 3.14 (2 знака после запятой)
print(f"pi = {pi:.4f}")         # 3.1416 (4 знака)

# Процент: {число:.2%}
rate = 0.856
print(f"Успешность: {rate:.1%}")  # 85.6%

# Разделение тысячи: {число:,}
amount = 1000000
print(f"Сумма: {amount:,}")     # 1,000,000 (с запятыми)


print("\n" + "=" * 55)
print("5) МНОГОСТРОЧНЫЕ СТРОКИ (тройные кавычки)")
print("=" * 55)

user = "Виктор"
balance = 500

# Многострочная строка
info = f"""
Профиль пользователя:
  Имя: {user}
  Баланс: {balance} руб.
  Статус: активен
"""
print(info)


print("\n" + "=" * 55)
print("6) МЕТОДЫ СТРОК: РЕГИСТР")
print("=" * 55)

text = "Hello World"

print(f"Оригинал:       '{text}'")
print(f"upper():        '{text.upper()}'")        # Все прописные
print(f"lower():        '{text.lower()}'")        # Все строчные
print(f"capitalize():   '{text.capitalize()}'")   # Первый символ заглавный
# Первая буква каждого слова заглавная
print(f"title():        '{text.title()}'")
print(f"swapcase():     '{text.swapcase()}'")     # Инвертировать регистр


print("\n" + "=" * 55)
print("7) МЕТОДЫ СТРОК: ПОИСК И ЗАМЕНА")
print("=" * 55)

text = "Hello World, Hello Python"

# find() — найти позицию подстроки (или -1)
pos = text.find("Hello")
print(f"Позиция 'Hello': {pos}")              # 0

pos = text.find("Hello", 10)                  # Начать поиск с позиции 10
print(f"Позиция 'Hello' с позиции 10: {pos}")  # 13

# count() — сколько раз встречается подстрока
count = text.count("Hello")
print(f"Сколько раз 'Hello': {count}")        # 2

# replace() — заменить все вхождения
replaced = text.replace("Hello", "Hi")
print(f"После замены: '{replaced}'")

# replace(old, new, count) — заменить первые N вхождений
replaced = text.replace("Hello", "Hi", 1)    # Только первое
print(f"Первое заменено: '{replaced}'")


print("\n" + "=" * 55)
print("8) МЕТОДЫ СТРОК: ПРОВЕРКА И ВЫДЕЛЕНИЕ")
print("=" * 55)

text = "Python"

# startswith() и endswith() — начинается/кончается ли на
print(f"Начинается на 'Py': {text.startswith('Py')}")       # True
print(f"Кончается на 'on': {text.endswith('on')}")          # True

# in — проверить содержимое (оператор, не метод)
print(f"'th' в 'Python': {'th' in text}")                   # True

# isdigit(), isalpha(), isalnum(), isspace() — тип символов
print(f"'123'.isdigit(): {'123'.isdigit()}")                # True
print(f"'abc'.isalpha(): {'abc'.isalpha()}")                # True
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")          # True
print(f"'   '.isspace(): {'   '.isspace()}")                # True


print("\n" + "=" * 55)
print("9) МЕТОДЫ СТРОК: ОЧИСТКА И РАЗБИЕНИЕ")
print("=" * 55)

# strip() — убрать пробелы в начале и конце
text = "  Hello World  "
print(f"Оригинал: '{text}'")
print(f"strip():  '{text.strip()}'")           # "Hello World"
print(f"lstrip(): '{text.lstrip()}'")          # "Hello World  " (левый край)
print(f"rstrip(): '{text.rstrip()}'")          # "  Hello World" (правый край)

# split() — разбить на список по разделителю
text = "apple,banana,orange"
fruits = text.split(",")
print(f"split(','): {fruits}")                 # ['apple', 'banana', 'orange']

# split() без аргумента — по пробелам
text = "one   two three"
words = text.split()
print(f"split():   {words}")                   # ['one', 'two', 'three']

# join() — объединить список в строку
words = ["Hello", "World", "Python"]
result = " ".join(words)
print(f"join():    '{result}'")                # "Hello World Python"


print("\n" + "=" * 55)
print("10) МЕТОДЫ СТРОК: ИНДЕКСЫ И СРЕЗЫ")
print("=" * 55)

text = "Python"

# Индексирование — доступ по номеру
print(f"text[0]: '{text[0]}'")                 # 'P'
print(f"text[-1]: '{text[-1]}'")               # 'n' (последний)

# Срезы — подстрока
# 'yth' (с индекса 1 до 4, не включая 4)
print(f"text[1:4]: '{text[1:4]}'")
print(f"text[:3]: '{text[:3]}'")               # 'Pyt' (с начала до 3)
print(f"text[3:]: '{text[3:]}'")               # 'hon' (с 3 до конца)
print(f"text[::2]: '{text[::2]}'")             # 'Pto' (каждый второй)


print("\n" + "=" * 55)
print("ИТОГ: когда что использовать?")
print("=" * 55)
print("""
f-строки:
[OK] Вставлять переменные в текст: f"Имя: {name}"
[OK] Вычисления: f"Сумма: {x + y}"
[OK] Форматирование: f"Число: {num:.2f}"
[OK] Вызывать методы: f"Прописные: {text.upper()}"

Методы строк:
[OK] upper(), lower() — изменить регистр
[OK] find(), count() — поиск
[OK] replace() — замена
[OK] startswith(), endswith() — проверка начала/конца
[OK] strip() — убрать пробелы
[OK] split() — разбить на части
[OK] join() — собрать из частей
[OK] isdigit(), isalpha() — проверка типа
[OK] [индекс] — доступ к символу
[OK] [начало:конец] — срез подстроки
""")
