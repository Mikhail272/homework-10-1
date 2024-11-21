from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Функция, которая возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    for i in transactions:
        if i["operationAmount"]["currency"]["code"] == currency:
            yield i


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Функция, которая возвращает описание каждой операции по очереди."""
    for i in transactions:
        yield i["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Функция, которая возвращает номера банковских карт
    в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    if (
        len(str(start)) > 16
        or len(str(end)) > 16
        or start > end
        or isinstance(start, str)
        or isinstance(end, str)
    ):
        yield ""
    else:
        for i in range(start, end + 1):
            text = (16 - len(str(i))) * "0" + str(i)
            yield " ".join(text[b * 4 : (b + 1) * 4] for b in range(4))
