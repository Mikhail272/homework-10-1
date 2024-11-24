from collections.abc import Iterator
from typing import Any, Dict, Generator, List


def filter_by_currency(list_of_transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]] | str:
    """Функция должна возвращает итератор, выдающий транзакции, где валюта операции соответствует заданной"""
    if not isinstance(list_of_transactions, list) or not isinstance(currency, str):
        raise TypeError("Ошибка типа данных")

    if len(list_of_transactions) > 0:
        filtered_transaction = filter(
            lambda x: x["operationAmount"]["currency"]["code"] == currency, list_of_transactions
        )
        return filtered_transaction
    else:
        return "Список пустой!"


def transaction_descriptions(list_of_transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """Генератор, принимающий список словарей с транзакциями и возвращающий описание каждой операции по очереди"""
    if not isinstance(list_of_transactions, list):
        raise TypeError("Ошибка типа данных")
    for transaction in list_of_transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генератор номеров банковских карт в формате 'XXXX XXXX XXXX XXXX'"""
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Ошибка типа данных")
    if stop < start:
        raise ValueError("Границы диапазона указаны неверно (в обратном порядке)!")
    if len(str(start)) <= 16:
        for number in range(start, stop + 1):
            formated_card_number = "{:016}".format(number)
            yield " ".join(formated_card_number[i * 4 : (i + 1) * 4] for i in range(4))
    else:
        raise ValueError("Входные данные превышают допустимые значения!!!")


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

# usd_transactions = filter_by_currency(transactions, "USD")
# try:
#     for i in range(2):
#         print(next(usd_transactions))
# except StopIteration:
#     print("Список пустой!")
#
# descriptions = transaction_descriptions([])
# try:
#     for i in range(5):
#         print(next(descriptions))
# except StopIteration:
#     print("Список пустой!")
#
# for card_number in card_number_generator(1, 5):
#     print(card_number)
