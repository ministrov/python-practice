""" Модуль для тренировки принципа ISP (Interface Segregation Principle)"""

# Простыми словами: класс не должен быть обязан реализовывать методы, которые ему не нужны.


class PaymentProcessor:
    def pay(self, amount: float):
        pass

    def refund(self, amount: float):
        pass

    def tokenize_card(self, card_number: str):
        pass

    def check_balance(self):
        pass
