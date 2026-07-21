# -*- coding: utf-8 -*-
"""
Блок 2.5.3: Демо — наследование, super(), MRO
════════════════════════════════════════════════════════════════════════
Темы:
  1. Наследование — класс-потомок получает всё от класса-родителя
  2. Переопределение метода (override) — потомок пишет свою версию
  3. super() — вызов версии родителя изнутри потомка (не дублировать код)
  4. super().__init__() — самый частый случай: дополнить конструктор
     родителя, а не переписывать его с нуля
  5. isinstance() / issubclass() — проверка принадлежности к иерархии
  6. MRO (Method Resolution Order) — порядок, в котором Python ищет
     метод при множественном наследовании
"""


# ════════════════════════════════════════════════════════════════════════
# 1. Простое наследование — Dog получает всё от Animal
# ════════════════════════════════════════════════════════════════════════

class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return f"{self.name} издаёт звук"


class Dog(Animal):
    # Dog ничего не переопределяет — просто наследует __init__ и speak
    pass


rex = Dog("Рекс")
print(rex.name)          # Рекс — атрибут пришёл от Animal
print(rex.speak())       # Рекс издаёт звук — метод пришёл от Animal
print(isinstance(rex, Dog))     # type: ignore[reportUnnecessaryIsInstance]
print(isinstance(rex, Animal))  # type: ignore[reportUnnecessaryIsInstance]
# Оба True — Dog ЯВЛЯЕТСЯ Animal тоже (проверки намеренно очевидны для
# демонстрации; pyright statically знает результат заранее)


# ════════════════════════════════════════════════════════════════════════
# 2. Переопределение метода (override)
# ════════════════════════════════════════════════════════════════════════

class Cat(Animal):
    def speak(self) -> str:
        # своя версия метода — полностью заменяет версию Animal
        return f"{self.name} говорит: Мяу!"


whiskers = Cat("Усы")
print(whiskers.speak())   # Усы говорит: Мяу! — своя версия, не от Animal


# ════════════════════════════════════════════════════════════════════════
# 3. super() — вызвать версию РОДИТЕЛЯ изнутри переопределённого метода
# ════════════════════════════════════════════════════════════════════════

class Cow(Animal):
    def speak(self) -> str:
        # сначала берём результат родителя, потом добавляем своё —
        # не дублируем f"{self.name} издаёт звук" вручную
        base = super().speak()
        return f"{base} (а именно: Му!)"


bessie = Cow("Бурёнка")
print(bessie.speak())     # Бурёнка издаёт звук (а именно: Му!)


# ════════════════════════════════════════════════════════════════════════
# 4. super().__init__() — самый частый паттерн: дополнить конструктор
# ════════════════════════════════════════════════════════════════════════

class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name: str, salary: float, team_size: int) -> None:
        # передаём name/salary родителю — он сам создаст self.name,
        # self.salary; не переписываем эту логику заново
        super().__init__(name, salary)
        self.team_size = team_size

    def describe(self) -> str:
        return (
            f"{self.name}: зарплата {self.salary}, "
            f"команда из {self.team_size} человек"
        )


boss = Manager("Ирина", 150000, 5)
print(boss.describe())    # Ирина: зарплата 150000, команда из 5 человек

# Без super().__init__() пришлось бы вручную повторять
# self.name = name; self.salary = salary — дублирование кода родителя


# ════════════════════════════════════════════════════════════════════════
# 5. issubclass() — проверка отношений МЕЖДУ КЛАССАМИ (не экземплярами)
# ════════════════════════════════════════════════════════════════════════

print(issubclass(Manager, Employee))  # type: ignore[reportUnnecessaryIsInstance]
print(issubclass(Employee, Manager))   # False — обратное неверно
print(issubclass(Dog, Animal))        # type: ignore[reportUnnecessaryIsInstance]
# True, False, True — первая и третья строки намеренно очевидны для
# демонстрации; pyright statically знает результат заранее


# ════════════════════════════════════════════════════════════════════════
# 6. MRO — порядок поиска метода при МНОЖЕСТВЕННОМ наследовании
# ════════════════════════════════════════════════════════════════════════

class Flyer:
    def move(self) -> str:
        return "летит"


class Swimmer:
    def move(self) -> str:
        return "плывёт"


class Duck(Flyer, Swimmer):
    # Duck не переопределяет move — какой move найдётся: от Flyer
    # или от Swimmer? Python ищет СЛЕВА НАПРАВО по списку родителей.
    pass


donald = Duck()
print(donald.move())   # летит — Flyer стоит первым в Duck(Flyer, Swimmer)

# __mro__ — сам порядок поиска, по которому Python обходит классы
print([cls.__name__ for cls in Duck.__mro__])
# ['Duck', 'Flyer', 'Swimmer', 'object']

# Если бы порядок родителей был Duck(Swimmer, Flyer) — move() дал бы
# "плывёт", а __mro__ начинался бы с ['Duck', 'Swimmer', 'Flyer', ...]
