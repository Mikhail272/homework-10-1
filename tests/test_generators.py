import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions


def test_filter_by_currency_usd(transactions_list, usd_transactions):
    result = filter_by_currency(transactions_list, "USD")
    assert next(result) == usd_transactions


def test_filter_by_currency_rub(transactions_list, rub_transactions):
    result = filter_by_currency(transactions_list, "RUB")
    assert next(result) == rub_transactions


def test_filter_by_currency_exceptions(transactions_list):
    result = filter_by_currency(transactions_list, "EUR")
    assert list(result) == []
    result = filter_by_currency([], "EUR")
    assert result == "Список пустой!"


def test_filter_by_currency_wrong_type():
    with pytest.raises(TypeError):
        next(filter_by_currency(1, [4, 3, 2]))
    with pytest.raises(TypeError):
        next(filter_by_currency("some_string", 2))
    with pytest.raises(TypeError):
        next(filter_by_currency(transactions, 2))
    with pytest.raises(TypeError):
        next(filter_by_currency(521, "USD"))


def test_transaction_descriptions(transactions_list):
    result = transaction_descriptions(transactions_list)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"


def test_transaction_descriptions_exceptions():
    with pytest.raises(StopIteration):
        next(transaction_descriptions([]))


def test_transaction_descriptions_wrong_type():
    with pytest.raises(TypeError):
        next(transaction_descriptions(1))
    with pytest.raises(TypeError):
        next(transaction_descriptions("some_string"))


@pytest.mark.parametrize('start, stop, expected', [(10, 12, ["0000 0000 0000 0010",
                                                             "0000 0000 0000 0011",
                                                             "0000 0000 0000 0012"]),
                                                   (5, 6, ["0000 0000 0000 0005",
                                                           "0000 0000 0000 0006"]),
                                                   (1000, 1002, ["0000 0000 0000 1000",
                                                                 "0000 0000 0000 1001",
                                                                 "0000 0000 0000 1002"])])
def test_card_number_generator(start, stop, expected):
    result = card_number_generator(start, stop)
    assert next(result) == expected[0]
    assert next(result) == expected[1]


def test_card_number_generator_wrong_type():
    with pytest.raises(TypeError):
        next(card_number_generator([1, 2, 3], 1))
    with pytest.raises(TypeError):
        next(card_number_generator(5, "some_string"))


def test_card_number_generator_boundary_values():
    result_max = card_number_generator(9999999999999998, 9999999999999999)
    assert next(result_max) == "9999 9999 9999 9998"
    assert next(result_max) == "9999 9999 9999 9999"


def test_card_number_generator_after_boundary_values():
    with pytest.raises(ValueError):
        next(card_number_generator(10000000000000000, 10000000000000001))


def test_card_number_generator_wrong_start_stop():
    with pytest.raises(ValueError):
        next(card_number_generator(7, 5))