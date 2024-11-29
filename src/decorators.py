from functools import wraps
import time
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор, который логирует начало и конец выполнения функции, а также ее результаты или ошибки."""

    def inner(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Логируем начало
            if filename is None or filename == "":
                print(f"Starting execution of {func.__name__}...")
            else:
                with open(filename, "a", encoding="utf-8") as log_file:
                    log_file.write(f"Starting execution of {func.__name__}...\n")

            try:
                result = func(*args, **kwargs)  # Вызов оригинальной функции
                # Логируем успешное завершение
                if filename is None or filename == "":
                    print(f"{func.__name__} ok. Result: {result}")
                else:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"{func.__name__} ok. Result: {result}\n")
                return result
            except Exception as er:
                # Логируем ошибку
                if filename is None or filename == "":
                    print(f"{func.__name__} error: {er}. Inputs: {args} {kwargs}")
                else:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"{func.__name__} error: {er}. Inputs: {args} {kwargs}\n")
                raise  # Здесь мы поднимаем исключение дальше
            finally:
                # Логируем окончание
                if filename is None or filename == "":
                    print(f"Finished execution of {func.__name__}.")
                else:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"Finished execution of {func.__name__}.\n")

        return wrapper

    return inner


def timing(func: Callable) -> Callable:
    """Декоратор, определяющий время работы функции, включая время начала и окончания."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()  # Запоминаем начало выполнения
        print(f"Start time for {func.__name__}: {time.asctime()}")

        result = func(*args, **kwargs)  # Вызов оригинальной функции

        end_time = time.time()  # Запоминаем окончание выполнения
        print(f"End time for {func.__name__}: {time.asctime()}")
        print(f"Time taken for {func.__name__}: {end_time - start_time:.4f} seconds")

        return result

    return wrapper


@timing
@log()  # Убедитесь, что декоратор log вызывается с пустыми скобками
def my_function(x: int | float, y: int | float) -> int | float:
    return x + y


my_function(1, 2)