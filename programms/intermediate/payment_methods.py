"""Модуль для тренировки принципа ISP (Interface Segregation Principle)"""

# Простыми словами: класс не должен быть обязан реализовывать методы, которые ему не нужны.

from abc import ABC, abstractmethod


class Payable(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

    @abstractmethod
    def refund(self, amount: float):
        pass


class Tokenizable(ABC):
    @abstractmethod
    def tokenize_card(self, card_number: str):
        pass


class BalanceCheckable(ABC):
    @abstractmethod
    def check_balance(self):
        pass


class Card(Payable, Tokenizable):
    def pay(self, amount: float):
        pass

    def refund(self, amount: float):
        pass

    def tokenize_card(self, card_number: str):
        pass


class Paypal(Payable, BalanceCheckable):
    def pay(self, amount: float):
        pass

    def refund(self, amount: float):
        pass

    def check_balance(self):
        pass
