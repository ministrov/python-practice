# -*- coding: utf-8 -*-
"""
Блок 2.5.9: Демо — 4 столпа ООП (итог блока)
════════════════════════════════════════════════════════════════════════
Новый синтаксис здесь НЕ вводится — все инструменты уже знакомы из
предыдущих тем. Задача этого файла — назвать словами то, что уже было
сделано практически, и собрать все 4 столпа в ОДНОЙ системе (иерархия
банковских счетов), чтобы было видно, как они работают вместе, а не
как четыре несвязанных примера.

Столпы:
  1. Инкапсуляция  — property + приватный атрибут  (уже было: 03_methods_demo.py, BankAccount)
  2. Абстракция    — abc.ABC + @abstractmethod       (уже было: 13_abstraction_demo.py)
  3. Наследование  — super().__init__()               (уже было: 05_inheritance_demo.py)
  4. Полиморфизм   — list[БазовыйТип] + override      (уже было: 14_abstraction_task.py, задание 7)
"""

from abc import ABC, abstractmethod


# ════════════════════════════════════════════════════════════════════════
# 1. ИНКАПСУЛЯЦИЯ — скрыть _balance, дать контролируемый доступ через
#    property (тот же приём, что и в BankAccount из 03_methods_demo.py)
# ════════════════════════════════════════════════════════════════════════

class Account(ABC):
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = balance   # "_balance" — приватное имя по конвенции

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._balance = value

    # ════════════════════════════════════════════════════════════════════
    # 2. АБСТРАКЦИЯ — Account(ABC) с abstractmethod: контракт есть, но
    #    у КАЖДОГО типа счёта своя ставка, поэтому реализации в базовом
    #    классе нет (тот же приём, что Shape/PaymentMethod в 13_abstraction_demo.py)
    # ════════════════════════════════════════════════════════════════════

    @abstractmethod
    def interest_rate(self) -> float:
        ...


try:
    account = Account("Anton", 100)  # type: ignore[misc]  # намеренно
except TypeError as e:
    print(f"Ошибка: {e}")
# Ошибка: Can't instantiate abstract class Account without an implementation
# for abstract method 'interest_rate' — как и в 13_abstraction_demo.py,
# ABC не даёт создать объект, пока контракт не выполнен


# ════════════════════════════════════════════════════════════════════════
# 3. НАСЛЕДОВАНИЕ — SavingsAccount реализует контракт (interest_rate),
#    переиспользуя __init__ родителя через super() (как Manager в
#    05_inheritance_demo.py), а не дублируя self.owner/self._balance
# ════════════════════════════════════════════════════════════════════════

class SavingsAccount(Account):
    def __init__(self, owner: str, balance: float, rate: float) -> None:
        super().__init__(owner, balance)
        self.rate = rate

    def interest_rate(self) -> float:
        return self.rate


class CheckingAccount(Account):
    def interest_rate(self) -> float:
        return 0.0   # расчётный счёт процентов не начисляет


savings = SavingsAccount("Anton", 1000, rate=0.05)
checking = CheckingAccount("Bella", 500)

print(savings.balance)            # 1000 — property из шага 1, унаследовано
print(savings.interest_rate())    # 0.05


# ════════════════════════════════════════════════════════════════════════
# 4. ПОЛИМОРФИЗМ — код работает со СПИСКОМ базового типа Account и не
#    знает, какой конкретно счёт перед ним (тот же приём, что animals:
#    list[Animal] в 14_abstraction_task.py, задание 7)
# ════════════════════════════════════════════════════════════════════════

accounts: list[Account] = [savings, checking]

for acc in accounts:
    projected = acc.balance * (1 + acc.interest_rate())
    print(f"{acc.owner}: {acc.balance} -> {projected}")
# Anton: 1000 -> 1050.0
# Bella: 500 -> 500.0
# Цикл вызывает acc.interest_rate() и читает acc.balance ОДИНАКОВО для
# обоих счетов — SavingsAccount и CheckingAccount вычисляют это по-разному,
# но вызывающий код это не видит и знать не должен


# ════════════════════════════════════════════════════════════════════════
# ИТОГ: все 4 столпа — это одна система, а не 4 отдельных примера
# ════════════════════════════════════════════════════════════════════════
# - Инкапсуляция:  Account.balance — property с валидацией (>= 0)
# - Абстракция:    Account(ABC).interest_rate() — контракт без реализации
# - Наследование:  SavingsAccount/CheckingAccount переиспользуют __init__
#                  родителя через super()
# - Полиморфизм:   list[Account] — вызывающий код работает с ЛЮБЫМ
#                  наследником одинаково, через общий интерфейс
