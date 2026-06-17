"""
ПРАКТИКА: match / case — задачи для закрепления
Реши эти две задачи, используя структурное сопоставление.

Запусти файл: python 10_match_case_tasks.py
"""

print("=" * 55)
print("ЗАДАЧА 1: Определение сезона")
print("=" * 55)

# Напиши функцию get_season(month: int) -> str
# По номеру месяца возвращай сезон:
# - 12, 1, 2 → "Зима"
# - 3, 4, 5 → "Весна"
# - 6, 7, 8 → "Лето"
# - 9, 10, 11 → "Осень"
# - другое → "Неизвестный месяц"
#
# Подсказка: используй case ... | ... | ... для нескольких значений в одном case

def get_season(month: int) -> str:
    match month:
        case 12 | 1 | 2:
            return "Зима"
        case 3 | 4 | 5:
            return "Весна"
        case 6 | 7 | 8:
            return "Лето"
        case 9 | 10 | 11:
            return "Осень"
        case _:
            return "Неизвестный месяц"


print(get_season(1))    # Зима
print(get_season(7))    # Лето
print(get_season(13))   # Неизвестный месяц


print("\n" + "=" * 55)
print("ЗАДАЧА 2: Чётность с guard")
print("=" * 55)

# Напиши функцию describe_number(n: int) -> str
# - Если число < 0 → "Отрицательное"
# - Если число == 0 → "Ноль"
# - Если число > 0 и чётное → "Положительное чётное: {число}"
# - Если число > 0 и нечётное → "Положительное нечётное: {число}"
#
# Подсказка: используй guard (case x if условие)

def describe_number(n: int) -> str:
    match n:
        case x if x < 0:
            return "Отрицательное"
        case 0:
            return "Ноль"
        case x if x % 2 == 0:
            return f"Положительное чётное: {x}"
        case _: 
            return f"Положительное нечётное: {x}"

print(describe_number(-5))   # Отрицательное
print(describe_number(0))    # Ноль
print(describe_number(4))    # Положительное чётное: 4
print(describe_number(7))    # Положительное нечётное: 7


print("\n" + "=" * 55)
print("ЗАДАЧА 3: Классификация оценок")
print("=" * 55)

# Напиши функцию grade_letter(score: int) -> str
# По числовой оценке верни букву:
# - 90-100 → "A" (отлично)
# - 80-89 → "B" (хорошо)
# - 70-79 → "C" (удовлетворительно)
# - 60-69 → "D" (проходной)
# - 0-59 → "F" (не прошел)
# - остальное → "Неверная оценка"
#
# Подсказка: используй диапазон вида case x if 90 <= x <= 100

def grade_letter(score: int) -> str:
    # YOUR CODE HERE:
    pass


print(grade_letter(95))      # A
print(grade_letter(85))      # B
print(grade_letter(75))      # C
print(grade_letter(65))      # D
print(grade_letter(45))      # F
print(grade_letter(150))     # Неверная оценка


print("\n" + "=" * 55)
print("ЗАДАЧА 4: Команды терминала")
print("=" * 55)

# Напиши функцию execute_command(cmd: str) -> str
# Переведи команду в описание:
# - "ls", "dir" → "Список файлов"
# - "cd" → "Смена директории"
# - "pwd" → "Текущая директория"
# - "rm", "del" → "Удаление файла"
# - "cat", "type" → "Чтение файла"
# - иное → "Неизвестная команда"
#
# Подсказка: используй pipe для нескольких синонимов

def execute_command(cmd: str) -> str:
    # YOUR CODE HERE:
    pass


print(execute_command("ls"))     # Список файлов
print(execute_command("cd"))     # Смена директории
print(execute_command("del"))    # Удаление файла
print(execute_command("git"))    # Неизвестная команда


print("\n" + "=" * 55)
print("ЗАДАЧА 5: Определение координатной четверти")
print("=" * 55)

# Напиши функцию find_quadrant(x: int, y: int) -> str
# По координатам (x, y) определи четверть плоскости:
# - x > 0, y > 0 → "Первая четверть (I)"
# - x < 0, y > 0 → "Вторая четверть (II)"
# - x < 0, y < 0 → "Третья четверть (III)"
# - x > 0, y < 0 → "Четвёртая четверть (IV)"
# - иное → "На оси координат"
#
# Подсказка: используй кортеж (x, y) в match и распаковку в case

def find_quadrant(x: int, y: int) -> str:
    # YOUR CODE HERE:
    pass


print(find_quadrant(3, 4))       # Первая четверть (I)
print(find_quadrant(-2, 5))      # Вторая четверть (II)
print(find_quadrant(-3, -1))     # Третья четверть (III)
print(find_quadrant(5, -2))      # Четвёртая четверть (IV)
print(find_quadrant(0, 5))       # На оси координат


print("\n" + "=" * 55)
print("ЗАДАЧА 6: Определение типа файла")
print("=" * 55)

# Напиши функцию get_file_type(filename: str) -> str
# По расширению файла определи тип:
# - .txt, .md → "Текстовый файл"
# - .jpg, .png, .gif → "Изображение"
# - .py, .js, .java → "Исходный код"
# - .mp4, .mkv, .avi → "Видео"
# - .zip, .rar, .7z → "Архив"
# - иное → "Неизвестный тип"
#
# Подсказка: используй .lower() для регистронезависимости

def get_file_type(filename: str) -> str:
    # YOUR CODE HERE:
    pass


print(get_file_type("document.txt"))     # Текстовый файл
print(get_file_type("photo.PNG"))        # Изображение
print(get_file_type("script.py"))        # Исходный код
print(get_file_type("movie.mp4"))        # Видео
print(get_file_type("backup.zip"))       # Архив
print(get_file_type("file.xyz"))         # Неизвестный тип


print("\n" + "=" * 55)
print("ЗАДАЧА 7: Анализ результата игры")
print("=" * 55)

# Напиши функцию analyze_game_result(score: int, time: int) -> str
# По очкам и времени определи результат:
# - score >= 100 и time < 60 → "Отличный результат!"
# - score >= 100 и time >= 60 → "Хороший результат"
# - score >= 50 → "Средний результат"
# - score > 0 → "Слабый результат"
# - score == 0 → "Ты проиграл"
# - score < 0 → "Ошибка: отрицательный счёт"
#
# Подсказка: используй guard (if) для комбинирования условий

def analyze_game_result(score: int, time: int) -> str:
    # YOUR CODE HERE:
    pass


print(analyze_game_result(150, 45))      # Отличный результат!
print(analyze_game_result(120, 90))      # Хороший результат
print(analyze_game_result(75, 120))      # Средний результат
print(analyze_game_result(25, 180))      # Слабый результат
print(analyze_game_result(0, 300))       # Ты проиграл
print(analyze_game_result(-10, 100))     # Ошибка: отрицательный счёт


print("\n" + "=" * 55)
print("ЗАДАЧА 8: Определение уровня доступа")
print("=" * 55)

# Напиши функцию get_access_level(role: str) -> str
# По роли пользователя верни уровень доступа:
# - "admin", "root" → "Полный доступ"
# - "moderator", "editor" → "Ограниченный доступ"
# - "user", "guest" → "Базовый доступ"
# - иное → "Доступ запрещён"
#
# Подсказка: используй pipe для группировки ролей

def get_access_level(role: str) -> str:
    # YOUR CODE HERE:
    pass


print(get_access_level("admin"))         # Полный доступ
print(get_access_level("moderator"))     # Ограниченный доступ
print(get_access_level("user"))          # Базовый доступ
print(get_access_level("hacker"))        # Доступ запрещён


print("\n" + "=" * 55)
print("ЗАДАЧА 9: Расчёт цены билета")
print("=" * 55)

# Напиши функцию calculate_ticket_price(age: int, is_student: bool) -> int
# Цена билета:
# - возраст < 3 → 0 (бесплатно)
# - возраст 3-12 → 100 (детский)
# - возраст 12-65 и is_student → 150 (студенческий)
# - возраст 12-65 → 250 (взрослый)
# - возраст >= 65 → 200 (пенсионный)
#
# Подсказка: используй pattern (age, is_student) с guards

def calculate_ticket_price(age: int, is_student: bool) -> int:
    # YOUR CODE HERE:
    pass


print(calculate_ticket_price(2, False))      # 0
print(calculate_ticket_price(8, False))      # 100
print(calculate_ticket_price(25, True))      # 150
print(calculate_ticket_price(30, False))     # 250
print(calculate_ticket_price(70, False))     # 200


print("\n" + "=" * 55)
print("ЗАДАЧА 10: Определение типа погоды")
print("=" * 55)

# Напиши функцию describe_weather(temp: int, is_raining: bool) -> str
# По температуре и дождю определи погоду:
# - temp <= -10 → "Очень холодно"
# - -10 < temp <= 0 и not is_raining → "Холодно и ясно"
# - -10 < temp <= 0 и is_raining → "Холодно и идёт дождь"
# - 0 < temp <= 15 → "Прохладно"
# - 15 < temp <= 25 → "Комфортно"
# - temp > 25 → "Жарко"
#
# Подсказка: используй кортеж (temp, is_raining) и guards

def describe_weather(temp: int, is_raining: bool) -> str:
    # YOUR CODE HERE:
    pass


print(describe_weather(-15, False))      # Очень холодно
print(describe_weather(-5, False))       # Холодно и ясно
print(describe_weather(-5, True))        # Холодно и идёт дождь
print(describe_weather(10, False))       # Прохладно
print(describe_weather(20, False))       # Комфортно
print(describe_weather(30, True))        # Жарко
