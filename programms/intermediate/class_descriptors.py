""" Модуль дескриптора класса """


class Positive:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: object, owner: type | None = None) -> float:
        instance_dict: dict[str, float] = vars(obj)
        return instance_dict[self.name]

    def __set__(self, obj: object, value: float) -> None:
        if value <= 0:
            raise ValueError(f"{self.name} должно быть больше нуля")
        instance_dict: dict[str, float] = vars(obj)
        instance_dict[self.name] = value


class Product:
    price = Positive("price")


p = Product()
p.price = 100
print(p.price)  # 100 — сработал __get__
