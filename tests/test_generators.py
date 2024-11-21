import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def test_filter_by_currency(lst_for_generator: list, empty_lsts: list) -> None:
    """Тестируем функцию filter_by_currency from src.generators"""
    usd_transactions_with_currency = filter_by_currency(lst_for_generator, "USD")
    assert next(usd_transactions_with_currency) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }

    assert next(usd_transactions_with_currency) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }

    with pytest.raises(StopIteration):
        usd_transactions_wo_currency = filter_by_currency(lst_for_generator, "")
        assert next(usd_transactions_wo_currency)

    with pytest.raises(StopIteration):
        usd_transactions_wo_currency = filter_by_currency(lst_for_generator, "EUR")
        assert next(usd_transactions_wo_currency)

    with pytest.raises(StopIteration):
        usd_transactions_empty_lst = filter_by_currency(empty_lsts, "USD")
        assert next(usd_transactions_empty_lst)


def test_transaction_descriptions(lst_for_generator: list, empty_lsts: list) -> None:
    """Функция тестирует transaction_descriptions from src.generators"""
    descriptions = transaction_descriptions(lst_for_generator)
    assert next(descriptions) == "Перевод организации"

    assert next(descriptions) == "Перевод со счета на счет"
    with pytest.raises(StopIteration):
        descriptions_empty_lst = transaction_descriptions(empty_lsts)
        assert next(descriptions_empty_lst)


@pytest.mark.parametrize(
    "start, stop, result",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (12345678, 12345679, ["0000 0000 1234 5678", "0000 0000 1234 5679"]),
        (
            1234123412341234,
            1234123412341235,
            ["1234 1234 1234 1234", "1234 1234 1234 1235"],
        ),
        (1234123412341234, 12341234123412352, [""]),
        ("1245", "2356", [""]),
        (10, 1, [""]),
    ],
)
def test_card_number_generator(start: int, stop: int, result: list) -> None:
    """Функция тестирует card_number_generator from src.generators"""
    generator = list(card_number_generator(start, stop))
    assert generator == result
