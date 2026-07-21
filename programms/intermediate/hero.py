""" Модуль для создания героя игры """


class Hero:
    """ Герой игры """

    def __init__(self, name: str):
        self.name = name
        self.hit_point = 100
        self.inventory: list[str] = []
        self.is_alive = True

    def take_damage(self, amount: int):
        """ Получение урона """
        if not self.is_alive:
            print(f"{self.name} уже повержен")
            return
        self.hit_point -= amount
        if self.hit_point <= 0:
            self.hit_point = 0
            self.is_alive = False
            print(f"{self.name} теперь повержен")
        else:
            print(f"{self.name} получил {amount} урона")

    def heal(self, amount: int):
        """ Восстановление здоровья """
        if not self.is_alive:
            print(f"{self.name} уже повержен")
        self.hit_point = min(self.hit_point + amount, 100)
        print(f"{self.name} восстановил {amount} HP. Текущие HP {self.hit_point}")

    def add_item(self, item: str):
        """ Добавление предмета в inventory"""
        self.inventory.append(item)
        print(f"{self.name} получил предмет {item}")

    def show_status(self):
        """ Показ статуса """
        status = "Жив" if self.is_alive else "Повержен"
        print(
            f"{self.name} - HP: {self.hit_point} - Инвентарь: {self.inventory} [{status}]")


hero = Hero("Вася")
hero.add_item("Меч")
hero.show_status()
hero.take_damage(30)
hero.take_damage(60)
hero.heal(50)
hero.show_status()
