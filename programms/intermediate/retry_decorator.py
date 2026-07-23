""" Модуль для Декоратора retry.

    Описание задачи: должен обрабатывать ошибки и повторять выполнение функции заданное количество раз
"""

import functools
import random
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def retry(times: int) -> Callable[[Callable[P, T]], Callable[P, T]]:
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except ValueError as e:
                    print(f"Попытка {attempt} не удалась: {e}")
                    if attempt == times:
                        print("Все попытки завершены")
                        raise
            raise RuntimeError("retry: times must be >= 1")
        return wrapper
    return decorator


@retry(times=3)
def unstable() -> None:
    """ Иногда падает с ошибкой """

    if random.random() < 0.7:
        raise ValueError("Ошибка соединения")


if __name__ == "__main__":
    unstable()
    print("Успех")
