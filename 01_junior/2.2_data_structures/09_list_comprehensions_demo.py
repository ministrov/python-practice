# -*- coding: utf-8 -*-
"""
Р‘Р»РѕРє 2.2.5: List Comprehensions (СЃРїРёСЃРєРѕРІС‹Рµ РІС‹СЂР°Р¶РµРЅРёСЏ)
в•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђв•ђ

List comprehension вЂ” СЌС‚Рѕ РєРѕРјРїР°РєС‚РЅС‹Р№ СЃРїРѕСЃРѕР± СЃРѕР·РґР°С‚СЊ РЅРѕРІС‹Р№ СЃРїРёСЃРѕРє РЅР° РѕСЃРЅРѕРІРµ
СЃСѓС‰РµСЃС‚РІСѓСЋС‰РµРіРѕ СЃРїРёСЃРєР°. Р’РјРµСЃС‚Рѕ С†РёРєР»Р° for РїРёС€РµРј РІС‹СЂР°Р¶РµРЅРёРµ РІ РєРІР°РґСЂР°С‚РЅС‹С… СЃРєРѕР±РєР°С….

РЎРёРЅС‚Р°РєСЃРёСЃ: [РІС‹СЂР°Р¶РµРЅРёРµ for СЌР»РµРјРµРЅС‚ in РєРѕР»Р»РµРєС†РёСЏ if СѓСЃР»РѕРІРёРµ]
"""

# ===== Р‘РђР—РћР’РћР• РРЎРџРћР›Р¬Р—РћР’РђРќРР• =====
print("=== Р‘РђР—РћР’РћР• РРЎРџРћР›Р¬Р—РћР’РђРќРР• ===\n")

# РћР±С‹С‡РЅС‹Р№ СЃРїРѕСЃРѕР± (С†РёРєР»)
numbers = [1, 2, 3, 4, 5]
doubled_loop = []
for x in numbers:
    doubled_loop.append(x * 2)
print(f"Р¦РёРєР»: {doubled_loop}")  # [2, 4, 6, 8, 10]

# List comprehension
numbers = [1, 2, 3, 4, 5]
doubled_comp = [x * 2 for x in numbers]
print(f"List comprehension: {doubled_comp}")  # [2, 4, 6, 8, 10]

print()

# ===== Р¤РР›Р¬РўР РђР¦РРЇ (if СѓСЃР»РѕРІРёРµ) =====
print("=== Р¤РР›Р¬РўР РђР¦РРЇ (if СѓСЃР»РѕРІРёРµ) ===\n")

# РћР±С‹С‡РЅС‹Р№ СЃРїРѕСЃРѕР±
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_loop = []
for x in numbers:
    if x % 2 == 0:
        even_loop.append(x)
print(f"Р¦РёРєР» (С‡С‘С‚РЅС‹Рµ): {even_loop}")  # [2, 4, 6, 8]

# List comprehension
even_comp = [x for x in numbers if x % 2 == 0]
print(f"List comprehension (С‡С‘С‚РЅС‹Рµ): {even_comp}")  # [2, 4, 6, 8]

print()

# ===== РўР РђРќРЎР¤РћР РњРђР¦РРЇ + Р¤РР›Р¬РўР РђР¦РРЇ =====
print("=== РўР РђРќРЎР¤РћР РњРђР¦РРЇ + Р¤РР›Р¬РўР РђР¦РРЇ ===\n")

# РћР±С‹С‡РЅС‹Р№ СЃРїРѕСЃРѕР±
numbers = [1, 2, 3, 4, 5, 6]
squared_even_loop = []
for x in numbers:
    if x % 2 == 0:
        squared_even_loop.append(x ** 2)
print(f"Р¦РёРєР» (РєРІР°РґСЂР°С‚С‹ С‡С‘С‚РЅС‹С…): {squared_even_loop}")  # [4, 16, 36]

# List comprehension
squared_even_comp = [x ** 2 for x in numbers if x % 2 == 0]
print(f"List comprehension (РєРІР°РґСЂР°С‚С‹ С‡С‘С‚РЅС‹С…): {squared_even_comp}")  # [4, 16, 36]

print()

# ===== Р РђР‘РћРўРђ РЎРћ РЎРўР РћРљРђРњР =====
print("=== Р РђР‘РћРўРђ РЎРћ РЎРўР РћРљРђРњР ===\n")

# РЎРґРµР»Р°С‚СЊ РІСЃРµ Р±СѓРєРІС‹ Р±РѕР»СЊС€РёРјРё
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Uppercase: {uppercase}")  # ['HELLO', 'WORLD', 'PYTHON']

# РџРѕР»СѓС‡РёС‚СЊ РґР»РёРЅС‹ СЃР»РѕРІ
lengths = [len(word) for word in words]
print(f"Р”Р»РёРЅС‹ СЃР»РѕРІ: {lengths}")  # [5, 5, 6]

# РћСЃС‚Р°РІРёС‚СЊ С‚РѕР»СЊРєРѕ СЃР»РѕРІР° СЃ 5+ Р±СѓРєРІ
long_words = [word for word in words if len(word) >= 5]
print(f"РЎР»РѕРІР° СЃ 5+ Р±СѓРєРІ: {long_words}")  # ['hello', 'world', 'python']

print()

# ===== Р’Р›РћР–Р•РќРќР«Р• LIST COMPREHENSIONS =====
print("=== Р’Р›РћР–Р•РќРќР«Р• LIST COMPREHENSIONS ===\n")

# РЎРѕР·РґР°С‚СЊ С‚Р°Р±Р»РёС†Сѓ СѓРјРЅРѕР¶РµРЅРёСЏ (РѕР±С‹С‡РЅС‹Р№ СЃРїРѕСЃРѕР±)
table_loop = []
for i in range(1, 4):
    for j in range(1, 4):
        table_loop.append((i, j, i * j))
print(f"Р¦РёРєР» (С‚Р°Р±Р»РёС†Р° СѓРјРЅРѕР¶РµРЅРёСЏ):")
for item in table_loop:
    print(f"  {item}")

# List comprehension (РІР»РѕР¶РµРЅРЅС‹Р№)
table_comp = [(i, j, i * j) for i in range(1, 4) for j in range(1, 4)]
print(f"List comprehension (С‚Р°Р±Р»РёС†Р° СѓРјРЅРѕР¶РµРЅРёСЏ):")
for item in table_comp:
    print(f"  {item}")

print()

# ===== РЈРЎР›РћР’РР• ELSE (if-else) =====
print("=== РЈРЎР›РћР’РР• ELSE (if-else) ===\n")

# РћР±С‹С‡РЅС‹Р№ СЃРїРѕСЃРѕР±
numbers = [1, 2, 3, 4, 5, 6]
even_odd_loop = []
for x in numbers:
    if x % 2 == 0:
        even_odd_loop.append("even")
    else:
        even_odd_loop.append("odd")
print(f"Р¦РёРєР» (С‡С‘С‚РЅРѕРµ/РЅРµС‡С‘С‚РЅРѕРµ): {even_odd_loop}")

# List comprehension
even_odd_comp = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"List comprehension (С‡С‘С‚РЅРѕРµ/РЅРµС‡С‘С‚РЅРѕРµ): {even_odd_comp}")

print()

# ===== DICT COMPREHENSION (РґР»СЏ СЃР»РѕРІР°СЂРµР№) =====
print("=== DICT COMPREHENSION (РґР»СЏ СЃР»РѕРІР°СЂРµР№) ===\n")

# РЎРѕР·РґР°С‚СЊ СЃР»РѕРІР°СЂСЊ {С‡РёСЃР»Рѕ: РµРіРѕ РєРІР°РґСЂР°С‚}
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x ** 2 for x in numbers}
print(f"Dict comprehension: {squares_dict}")  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# РЎР»РѕРІР°СЂСЊ С‚РѕР»СЊРєРѕ С‡С‘С‚РЅС‹С…
even_squares = {x: x ** 2 for x in numbers if x % 2 == 0}
print(f"Р§С‘С‚РЅС‹Рµ РєРІР°РґСЂР°С‚С‹: {even_squares}")  # {2: 4, 4: 16}

# РРЅРІРµСЂС‚РёСЂРѕРІР°С‚СЊ СЃР»РѕРІР°СЂСЊ (РєР»СЋС‡Рё в†” Р·РЅР°С‡РµРЅРёСЏ)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"РРЅРІРµСЂС‚РёСЂРѕРІР°РЅРЅС‹Р№ СЃР»РѕРІР°СЂСЊ: {inverted}")  # {1: 'a', 2: 'b', 3: 'c'}

print()

# ===== SET COMPREHENSION (РґР»СЏ РјРЅРѕР¶РµСЃС‚РІ) =====
print("=== SET COMPREHENSION (РґР»СЏ РјРЅРѕР¶РµСЃС‚РІ) ===\n")

# РЎРѕР·РґР°С‚СЊ РјРЅРѕР¶РµСЃС‚РІРѕ РєРІР°РґСЂР°С‚РѕРІ
numbers = [1, 2, 3, 2, 1]
squares_set = {x ** 2 for x in numbers}
print(f"Set comprehension: {squares_set}")  # {1, 4, 9}

# РњРЅРѕР¶РµСЃС‚РІРѕ РґР»РёРЅ СЃР»РѕРІ
words = ["hello", "world", "hi", "python", "a"]
lengths_set = {len(word) for word in words}
print(f"РњРЅРѕР¶РµСЃС‚РІРѕ РґР»РёРЅ СЃР»РѕРІ: {lengths_set}")  # {1, 2, 5, 6}

print()

# ===== GENERATOR EXPRESSION (РіРµРЅРµСЂР°С‚РѕСЂРЅРѕРµ РІС‹СЂР°Р¶РµРЅРёРµ) =====
print("=== GENERATOR EXPRESSION (РіРµРЅРµСЂР°С‚РѕСЂ) ===\n")

# List comprehension вЂ” СЃРѕР·РґР°С‘С‚ РІРµСЃСЊ СЃРїРёСЃРѕРє СЃСЂР°Р·Сѓ РІ РїР°РјСЏС‚Рё
list_comp = [x ** 2 for x in range(5)]
print(f"List comprehension: {list_comp}")  # [0, 1, 4, 9, 16]

# Generator expression вЂ” СЃРѕР·РґР°С‘С‚ СЌР»РµРјРµРЅС‚С‹ РїРѕ РѕРґРЅРѕРјСѓ (Р»РµРЅРёРІС‹Рµ РІС‹С‡РёСЃР»РµРЅРёСЏ)
gen_exp = (x ** 2 for x in range(5))
print(f"Generator expression: {gen_exp}")  # <generator object ...>

# РњРѕР¶РЅРѕ РёС‚РµСЂРёСЂРѕРІР°С‚СЊ РіРµРЅРµСЂР°С‚РѕСЂ
print("Р­Р»РµРјРµРЅС‚С‹ РіРµРЅРµСЂР°С‚РѕСЂР°:")
for value in gen_exp:
    print(f"  {value}")

# РџРѕСЃР»Рµ РёС‚РµСЂР°С†РёРё РіРµРЅРµСЂР°С‚РѕСЂ РёСЃС‡РµСЂРїР°РЅ
print(f"Р•С‰С‘ СЂР°Р· iterire: {list(gen_exp)}")  # []

print()

# ===== РџР РђРљРўРР§Р•РЎРљРР• РџР РРњР•Р Р« =====
print("=== РџР РђРљРўРР§Р•РЎРљРР• РџР РРњР•Р Р« ===\n")

# 1. РР·РІР»РµС‡СЊ РёРјРµРЅР° РёР· СЃРїРёСЃРєР° РєРѕСЂС‚РµР¶РµР№
students = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]
names = [name for name, score in students]
print(f"РРјРµРЅР° СЃС‚СѓРґРµРЅС‚РѕРІ: {names}")  # ['Alice', 'Bob', 'Charlie']

# 2. Р¤РёР»СЊС‚СЂРѕРІР°С‚СЊ РїРѕ СѓСЃР»РѕРІРёСЋ
scores = [45, 78, 92, 88, 34, 76]
passed = [score for score in scores if score >= 70]
print(f"РџСЂРѕС€РµРґС€РёРµ (в‰Ґ70): {passed}")  # [78, 92, 88, 76]

# 3. РџСЂРµРѕР±СЂР°Р·РѕРІР°С‚СЊ СЃС‚СЂРѕРєРё РІ С‡РёСЃР»Р°
strings = ["1", "2", "3", "4", "5"]
numbers = [int(s) for s in strings]
print(f"Р§РёСЃР»Р°: {numbers}")  # [1, 2, 3, 4, 5]

# 4. РЎРѕР·РґР°С‚СЊ РІР»РѕР¶РµРЅРЅС‹Р№ СЃРїРёСЃРѕРє
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"РњР°С‚СЂРёС†Р°:")
for row in matrix:
    print(f"  {row}")

# 5. РћР±СЉРµРґРёРЅРёС‚СЊ РЅРµСЃРєРѕР»СЊРєРѕ СЃРїРёСЃРєРѕРІ
list1 = [1, 2, 3]
list2 = [4, 5]
combined = [x for lst in [list1, list2] for x in lst]
print(f"РћР±СЉРµРґРёРЅС‘РЅРЅС‹Рµ: {combined}")  # [1, 2, 3, 4, 5]

