"""Модуль для тренировки третьего принципа LSP (Liskov Substitution Principle)"""

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


@dataclass
class Installment(Payment):
    part: int

    def pay(self, amount: float) -> float:
        final = amount / self.part
        print(f"Списано: {final}")
        return final


def make_payment(payment: Payment, amount: float) -> float:
    return payment.pay(amount)


make_payment(Payment(), 1000)
make_payment(BonusPayment(bonuses=200), 1000)
make_payment(Installment(part=4), 1000)
