""" Модуль для тренировки принципа DIP (Dependency Inversion Principle)"""

# Модули верхних уровней не должны зависеть от модулей нижних уровней

from dataclasses import dataclass
from typing import Protocol


class StockRepository(Protocol):
    def get_stock_count(self) -> int: ...


@dataclass
class LowStockService:
    def run(self):
        pass
