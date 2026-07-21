""" Модуль для создания героя игры """


class Hero:
    def __init__(self, name: str):
        self.name = name
        self.hit_point = 100
        self.inventory: list[str] = []
        self.is_alive = True

    def take_damage(self, amount: int):
        if not self.is_alive:
            print(f"{self.name} уже повержен")
