"""Модуль для отработки принципа открытости и закрытости (Open/Close Principle)"""

# Классы должны быть открыты для расширения, но закрыты для модификации

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...


class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[Email] Отправлено сообщение: {message}")


class PushNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[Push] Отправлено сообщение: {message}")


class TelegramNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[Telegram] Отправлено сообщение: {message}")


@dataclass
class NotificationService:
    notifier: Notifier

    def send(self, message: str):
        self.notifier.send(message)


service = NotificationService(EmailNotifier())
service.send("Привет")
