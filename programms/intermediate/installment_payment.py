""" Модуль для тренировки третьего принципа LSP (Liskov Substitution Principle)"""


from dataclasses import dataclass


class Payment:
    def pay(self, amount: float) -> float:
        print(f"Списано: {amount}")
        return amount


@dataclass
class BonusPayment(Payment):
    bonuses: float

    def pay(self, amount: float) -> float:
        final = amount - self.bonuses
        print(f"Списано: {final}")
        return final


class Installment(Payment):
    pass
